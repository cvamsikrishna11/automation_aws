import json
import boto3


def lambda_handler(event, context):
    # TODO implement
    ec2_con = boto3.resource(service_name='ec2', region_name='ap-southeast-1')
    sns_client = boto3.client(service_name='sns', region_name='ap-southeast-1')
    my_ins = ec2_con.Instance('i-123445827634')
    print(my_ins.state['Name'])

    sns_client.publish(TargetArn='arn:aws:sns:ap-southeast-1:ACCOUNTID:Vamsi_ec2', Message=my_ins.state['Name'])
