import boto3

aws_mag_con = boto3.session.Session(profile_name='vamsi')
iam_con_re = aws_mag_con.resource(service_name='iam')

for each_group in iam_con_re.groups.all():
    print(each_group)
