import boto3
import datetime

aws_mag_con = boto3.session.Session(profile_name='vamsi')
ec2_con_re = aws_mag_con.resource(service_name='ec2', region_name='ap-southeast-1')
sts_con_cli = aws_mag_con.client(service_name='sts', region_name='ap-southeast-1')
response = sts_con_cli.get_caller_identity()
my_aws_id = response.get('Account')

today = datetime.datetime.now()
start_time = datetime.datetime(today.year, today.month, today.day, 6, 15, 30)
print(start_time)
size_filter = {'Name': 'volume-size', 'Values': ['8']}
for each in ec2_con_re.snapshots.filter(OwnerIds=[my_aws_id]):
    # if each.start_time.strftime('%Y-%m-%d %H:%M:%S') == start_time:
    print(each.id, each.start_time.strftime('%Y-%m-%d %H:%M:%S'))
