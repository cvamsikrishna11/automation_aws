import boto3

aws_mag_con = boto3.session.Session(profile_name='vamsi')
iam_con_re = aws_mag_con.resource(service_name='iam')

# get details of any IAM user
iam_user_response = iam_con_re.User('vamsi_chunduru')

print(iam_user_response.user_name)

# all
for each_user in iam_con_re.users.all():
    print(dir(each_user))