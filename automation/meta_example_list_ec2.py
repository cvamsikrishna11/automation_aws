import boto3

'''
convert from resource to client
'''
aws_mag_con = boto3.session.Session(profile_name='vamsi')

ec2_con_re = aws_mag_con.resource(service_name='ec2')

for each_item in ec2_con_re.meta.client.describe_regions()['Regions']:
    print(each_item)
