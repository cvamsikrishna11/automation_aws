import boto3
from boto3.dynamodb.conditions import Attr, Key
import botocore

##############################################################################
# This file have all the basic operations at table and item level of DynamoDB
##############################################################################
aws_profile = boto3.session.Session(profile_name='vamsi')
dynamodb_resource = aws_profile.resource(service_name='dynamodb', region_name='us-east-1')
dynamodb_client = aws_profile.client(service_name='dynamodb', region_name='us-east-1')


def basic_operations():
    table_name = 'td_notes'

    # list all tables, print names
    for each_table in dynamodb_resource.tables.all():
        print("table name:", each_table.table_name)

    # get particular table obj
    table = dynamodb_resource.Table(table_name)
    print("table obj:", table)

    # describe a table, with client obj
    table = dynamodb_client.describe_table(TableName=table_name)
    print(table)


# create a dynamo db table with client obj
def create_dynamodb_table():
    new_table = dynamodb_client.create_table(TableName='td_notes_sdk',
                                             AttributeDefinitions=[
                                                 {
                                                     'AttributeName': 'user_id',
                                                     'AttributeType': 'S'
                                                 },
                                                 {
                                                     'AttributeName': 'timestamp',
                                                     'AttributeType': 'N'
                                                 }
                                             ],
                                             KeySchema=[
                                                 {
                                                     'AttributeName': 'user_id',
                                                     'KeyType': 'HASH'
                                                 },
                                                 {
                                                     'AttributeName': 'timestamp',
                                                     'KeyType': 'RANGE'
                                                 }
                                             ],
                                             ProvisionedThroughput={
                                                 'ReadCapacityUnits': 1,
                                                 'WriteCapacityUnits': 1
                                             }
                                             )
    return new_table


# update dynamodb table configurations
def update_table_configs():
    response = dynamodb_client.update_table(
        TableName='td_notes_sdk',
        ProvisionedThroughput={
            'ReadCapacityUnits': 2,
            'WriteCapacityUnits': 1
        }
    )
    return response


# to put item
def put_item():
    response = dynamodb_client.put_item(
        TableName='td_notes_sdk',
        Item={
            'user_id': {'S': 'cc'},
            'timestamp': {'N': '21'},
            'title': {'S': 'third title'},
            'content': {'S': 'third content'}
        }
    )
    return response


# get item
def get_item():
    response = dynamodb_client.get_item(
        TableName='td_notes_sdk',
        Key={
            'user_id': {'S': 'bb'},
            'timestamp': {'N': '2'}
        }
    )
    return response['Item']


# update item
def update_item():
    response = dynamodb_client.update_item(
        TableName='td_notes_sdk',
        Key={
            'user_id': {'S': 'bb'},
            'timestamp': {'N': '2'}
        },
        UpdateExpression='SET title = :val1',
        ExpressionAttributeValues={
            ':val1': {'S': 'Updated title'}
        }
    )
    return response


# delete item
def delete_item():
    response = dynamodb_client.delete_item(
        TableName='td_notes_sdk',
        Key={
            'user_id': {'S': 'cc'},
            'timestamp': {'N': '21'}
        }
    )
    return response


# batch writing in loop
def batch_writing():
    table = dynamodb_resource.Table('td_notes_sdk')
    with table.batch_writer() as batch:
        batch.delete_item(
            Key={
                "user_id": "bb",
                "timestamp": 2
            }
        )
        batch.put_item(
            Item={
                'user_id': 'vamsi',
                'timestamp': 21,
                'title': 'third title',
                'content': 'third content'
            }
        )
        batch.put_item(
            Item={
                'user_id': 'krishna',
                'timestamp': 21,
                'title': 'third title',
                'content': 'third content'
            }
        )


# batch writing in loop
def batch_writing_iterator():
    table = dynamodb_resource.Table('td_notes_sdk')
    with table.batch_writer() as batch:
        for i in range(9):
            batch.put_item(
                Item={
                    "content": "content" + str(i),
                    "timestamp": i,
                    "title": "title" + str(i),
                    "user_id": "user" + str(i)
                }
            )


# put item based on condition
def conditional_writes():
    try:
        table = dynamodb_resource.Table('td_notes_sdk')
        response = table.put_item(
            TableName='td_notes_sdk',
            Item={
                'user_id': 'vamsi krishna chunduru',
                'timestamp': 2,
                'title': 'conditional write',
                'content': 'conditional write'
            },
            ConditionExpression=Attr("timestamp").ne(2),
            # ExpressionAttributeNames={
            #     '#column_name': 'timestamp'
            # },
            # ExpressionAttributeValues={
            #     ':column_value':
            #         {
            #             'N': 210
            #         }
            # }
        )
        return response
    except botocore.exceptions.ClientError as e:
        # Ignore the ConditionalCheckFailedException, bubble up
        # other exceptions.
        # based on our DB requirement we can trigger the exception
        if e.response['Error']['Code'] != 'ConditionalCheckFailedException':
            raise


# query the table
def query_table():
    table = dynamodb_resource.Table('td_notes_sdk')
    response = table.query(
        KeyConditionExpression=Key('user_id').eq('vamsi krishna chunduru'),
        FilterExpression=Attr('content').eq('conditional write')
    )
    items = response['Items']
    return items


# query the table
def query_on_index():
    table = dynamodb_resource.Table('td_notes_sdk')
    response = table.query(
        IndexName='content-index',
        KeyConditionExpression=Key('content').eq('content1')
    )
    items = response['Items']
    return items


# scan the table
def scan_table():
    table = dynamodb_resource.Table('td_notes_sdk')
    response = table.scan(
        FilterExpression=Attr('content').eq('third content')
    )
    items = response['Items']
    return items


# get batch items, to get more than one item from single or multiple tables at the same time
def batch_get_items():
    response = dynamodb_client.batch_get_item(
        RequestItems={
            'td_notes_sdk': {
                'Keys': [
                    {
                        "user_id": {"S": "vamsi"},
                        "timestamp": {"N": "21"}
                    },
                    {
                        "user_id": {"S": "vamsi krishna chunduru"},
                        "timestamp": {"N": "21"}
                    }

                ]
            },
            'td_notes': {
                'Keys': [
                    {
                        "user_id": {"S": "sljdfh1219"},
                        "timestamp": {"S": "23423421"}

                    },
                    {
                        "user_id": {"S": "ksjdfsjb97ya"},
                        "timestamp": {"S": "1584391148"}
                    }

                ]
            }
        }
    )
    return response


# pagination for scan
def scan_paginator():
    table = dynamodb_resource.Table('td_notes_sdk')
    response = table.scan()
    items = response['Items']
    while True:
        if response.get('LastEvaluatedKey'):
            response = table.scan(
                ExclusiveStartKey=response['LastEvaluatedKey']
            )
            items.extend(response['Items'])
        else:
            break
    return items


# pagination for query
def query_paginator():
    table = dynamodb_resource.Table('td_notes_sdk')
    response = table.query(KeyConditionExpression=Key('user_id').eq('vamsi'))
    items = response['Items']
    while True:
        if response.get('LastEvaluatedKey'):
            response = table.query(
                KeyConditionExpression=Key('user_id').eq('vamsi'),
                ExclusiveStartKey=response['LastEvaluatedKey']
            )
            items.extend(response['Items'])
        else:
            break
    return items


# delete dynamodb table
def delete_table():
    response = dynamodb_client.delete_table(
        TableName='td_notes_sdk'
    )
    return response

# basic_operations()
# print(create_dynamodb_table())
# print(update_table_configs())
# print(put_item())
# print(get_item())
# print(update_item())
# print(delete_item())
# batch_writing()
# batch_writing_iterator()
# print(conditional_writes())
# print(query_table())
# print(query_on_index())
# print(scan_table())
# print(batch_get_items())
# print(scan_paginator())
# print(query_paginator())
# print(delete_table())
