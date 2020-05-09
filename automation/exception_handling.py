import sys

import botocore

try:
    import boto3
except ModuleNotFoundError:
    print('Boto3 is not installed, please insrall boto3 and try again')
    sys.exit(1)
except Exception as e:
    print(e)
    sys.exit(2)
try:
    aws_mag_con = boto3.session.Session(profile_name='vamsi')
except botocore.exceptions.ProfileNotFound as e:
    print(e)
    print('dev profile is not configure on your .aws credentials file, Use other profile or please configure ')
    sys.exit(3)
except Exception as e:
    print(e)
    sys.exit(4)
try:
    iam_con_re = aws_mag_con.resource(service_name='iam')
    for each_user in iam_con_re.users.all():
        print(each_user)
except botocore.exceptions.ClientError as e:
    print(e)
    print('This is a client error exception')
except Exception as e:
    print(e)
    sys.exit(5)
