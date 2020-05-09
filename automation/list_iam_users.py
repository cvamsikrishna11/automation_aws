import boto3

aws_mag_con = boto3.session.Session(profile_name='vamsi')
aws_mag_cli = boto3.session.Session(profile_name='vamsi')

iam_con_re = aws_mag_con.resource(service_name='iam', region_name='ap-southeast-1')
iam_con_cli = aws_mag_cli.client(service_name='iam', region_name='ap-southeast-1')

# listing IAM users with resource obj
for each in iam_con_re.users.all():
    print(each.name)

# listing IAM users with client
for each in iam_con_cli.list_users()['Users']:
    print(each['UserName'])
