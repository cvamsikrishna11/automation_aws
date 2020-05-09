import boto3

aws_mag_con = boto3.session.Session(profile_name='vamsi')

iam_con_cli = aws_mag_con.client(service_name='iam', region_name='ap-southeast-1')
ec2_con_cli = aws_mag_con.client(service_name='ec2', region_name='ap-southeast-1')
s3_con_cli = aws_mag_con.client(service_name='s3', region_name='ap-southeast-1')

for val in iam_con_cli.list_users()['Users']:
    print(val['UserName'])

for val in ec2_con_cli.describe_instances()['Reservations']:
    for item in val['Instances']:
        print(item['InstanceId'])
