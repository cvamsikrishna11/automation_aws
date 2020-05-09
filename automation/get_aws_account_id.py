import boto3

aws_mag_con = boto3.session.Session(profile_name='vamsi')

sts_con_cli = aws_mag_con.client(service_name='sts', region_name='ap-southeast-1')

sts_response = sts_con_cli.get_caller_identity()
print('Account id:', sts_response['Account'])
print('User ID:', sts_response['UserId'])
