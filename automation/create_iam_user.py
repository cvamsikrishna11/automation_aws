import boto3
from random import choice
import sys


def get_iam_client_obj():
    aws_mag_con = boto3.session.Session(profile_name='vamsi')
    iam_con_cli = aws_mag_con.client(service_name='iam', region_name='ap-southeast-1')
    return iam_con_cli


def get_random_password():
    len_of_password = 8
    valid_chars_for_password = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$'

    print(choice(valid_chars_for_password))

    password = []
    for each_char in range(len_of_password):
        password.append(choice(valid_chars_for_password))

    rand_pass = ''.join(password)
    print(rand_pass)

    # in a single line
    rand_pass1 = ''.join(choice(valid_chars_for_password) for each_char in range(len_of_password))
    print(rand_pass1)
    return rand_pass1


def create_iam_user():
    iam_client = get_iam_client_obj()
    iam_user_name = 'vamsi.chunduru@tcs.com'
    password = get_random_password()
    policyArn = 'arn:aws:iam::ACCOUNTID:policy/ACME_Policy'
    try:
        iam_client.create_user(
            UserName=iam_user_name
        )
    except Exception as e:
        if e.response['Error']['Code'] == 'EntryAlreadyExists':
            print('Already IAM user with {} is exists'.format(iam_user_name))
        elif e.response['Error']['Code'] == 'PasswordPolicyViolationException':
            print('Password does not conform to the account password policy')
        else:
            print('Please verify the following error and retry...')
            print(e)

            sys.exit(0)
    iam_client.create_login_profile(UserName=iam_user_name, Password=password, PasswordResetRequired=False)
    iam_client.attach_user_policy(
        UserName=iam_user_name,
        PolicyArn=policyArn
    )
    print('IAM user name={} and password={}'.format(iam_user_name, password))


if __name__ == '__main__':
    create_iam_user()
