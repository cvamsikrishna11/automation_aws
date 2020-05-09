import json
import boto3

client = boto3.client('lambda')


def lambda_handler(event, context):
    number = event['number']
    payload = {
        "operation": "multiply",
        "input": {
            "operand1": number,
            "operand2": number
        }
    }
    print(json.dumps(payload).encode('utf-8'))
    payload_bytes = json.dumps(payload).encode('utf-8')
    response = client.invoke(
        FunctionName='lambda_calculator_post_example',
        InvocationType='RequestResponse',
        Payload=payload_bytes
    )
    return json.loads(response['Payload'].read().decode("utf-8"))
