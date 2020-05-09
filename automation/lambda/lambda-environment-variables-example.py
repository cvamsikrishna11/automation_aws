import os


def lambda_handler(event, context):
    # TODO implement
    return {
        'appName': os.environ['APP_NAME'],
        'appSecret': os.environ['APP_SECRET']

    }
