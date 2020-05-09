import logging

import boto3


##############################################################################################################
# This file have logging utility which can be used in local and lambda,
# Need to check the log duplication issue in lambda
##############################################################################################################
def log(name):
    """
    :param name: name of the function for logger profile
    :return: logger object
    """
    # Gets or creates a logger
    logger = logging.getLogger(name)
    # set log level
    logger.setLevel(logging.INFO)
    # define file handler and set formatter
    logger.handlers = []  # <== SOLUTION HERE FOR LAMBDA LOG DUPLICATION
    file_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s :: %(name)s :: %(funcName)s :: %(levelname)s :: %(message)s')
    file_handler.setFormatter(formatter)
    # add file handler to logger
    logger.addHandler(file_handler)
    return logger


def lambda_handler(event, context):
    client = boto3.client('sts')
    account_id = client.get_caller_identity()['Account']
    log(__name__).info('Getting account ID...')
    log(__name__).debug('Account ID: {}'.format(account_id))
    return account_id
