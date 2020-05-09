import json


##############################################################################################
# This file have simple calculator method in lambda, proper API gateway needs to be configured
##############################################################################################

def lambda_handler(event, context):
    operand1 = event['input']['operand1']
    operand2 = event['input']['operand2']
    switcher = {
        'add': operand1 + operand2,
        'subtract': operand1 - operand2,
        'multiply': operand1 * operand2,
        'divide': operand1 / operand2,
        None: None
    }
    response = {
        'result': switcher.get(event['operation'])
    }
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }


if __name__ == '__main__':
    event = {
        "operation": "add",
        "input": {
            "operand1": 5,
            "operand2": 2
        }
    }
    print(lambda_handler(event, 'test'))
