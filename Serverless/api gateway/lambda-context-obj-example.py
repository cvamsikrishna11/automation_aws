import json
import time
import logging

##############################################################################################
# This file have lambda context object example and operations
##############################################################################################
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def greet(arg_name):
    return 'hello ' + arg_name


def lambda_handler(event, context):
    print("Log stream name:", context.log_stream_name)
    print("Log group name:", context.log_group_name)
    print("Request ID:", context.aws_request_id)
    print("Mem. limits(MB):", context.memory_limit_in_mb)
    # Code will execute quickly, so we add a 1 second intentional delay so you can see that in time remaining value.
    time.sleep(1)
    print("Time remaining (MS):", context.get_remaining_time_in_millis())
    print("cognito identity:", context.identity)
    print(context.function_name)
    print(context.function_version)
    print(context.invoked_function_arn)
    logger.info('Message at the INFO level.')
    logger.debug('Message at the DEBUG level.')
    return {
        'statusCode': 200,
        'body': json.dumps(greet(event['name']))
    }
