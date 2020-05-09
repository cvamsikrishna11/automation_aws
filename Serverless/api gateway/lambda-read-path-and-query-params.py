import time
import json

greetings = {
    'en': 'hello',
    'fr': 'bonjour',
    'hi': 'namaste',
    'es': 'hola',
    'pt': 'ola',
    'ur': 'assalamo aleikum',
    'it': 'ciao',
    'de': 'hallo'
}


#####################################################################################################################
# To read path and query params from the lambda event object
# Proper API need to be setup in the API gateway,or event type in lambda test event input
#####################################################################################################################
def lambda_handler(event, context):
    name = event['pathParameters']['name']
    info = event['queryStringParameters']
    if (event['queryStringParameters'] is not None) and ('lang' in event['queryStringParameters'].keys()):
        language = event['queryStringParameters']['lang']
    else:
        language = None
    if language in greetings.keys():
        msg = greetings[language] + ' ' + name
    else:
        msg = greetings['en'] + ' ' + name
    response = {
        'message': msg,
        'time': time.time(),
        'info': info
    }
    return {
        'statusCode': 200,
        # to allow other domains when we use lambda proxy, if not normal proxy we can configure in API Gateway method
        # response itself
        'headers': {
            'Access-Control-Allow-Origin': 'test-cors.org'
        },
        'body': json.dumps(response)
    }
