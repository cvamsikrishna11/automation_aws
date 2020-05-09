import boto3

aws_mag_con = boto3.session.Session(profile_name='vamsi')
iam_con_re = aws_mag_con.resource(service_name='iam', region_name='ap-southeast-1')
ec2_con_res = aws_mag_con.resource(service_name='ec2', region_name='ap-southeast-1')
s3_con_res = aws_mag_con.resource(service_name='s3', region_name='ap-southeast-1')

# list all IAM users
iam_response = iam_con_re.users.all()
for value in iam_response:
    print(value.name)

# list EC2 ID's
ec2_response = ec2_con_res.instances.all()
for val in ec2_response:
    print(val.id)

# list s3 buckets

s3_response = s3_con_res.buckets.all()
for val in s3_response:
    print(val.name)
