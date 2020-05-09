import boto3

aws_mag_con = boto3.session.Session(profile_name='vamsi')

ec2_con_re = aws_mag_con.resource(service_name='ec2', region_name='ap-southeast-1')
# for each in ec2_con_re.snapshots.all():
#     print(each)

sts_con_cli = aws_mag_con.client(service_name='sts', region_name='ap-southeast-1')
response = sts_con_cli.get_caller_identity()
my_aws_id = response.get('Account')

for each in ec2_con_re.snapshots.filter(OwnerIds=[my_aws_id]):
    print(each)
