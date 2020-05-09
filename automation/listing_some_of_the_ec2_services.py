import boto3

aws_mag_con = boto3.session.Session(profile_name='vamsi')
ec2_con_cli = aws_mag_con.client(service_name='ec2', region_name='ap-southeast-1')

ec2_response = ec2_con_cli.describe_instances()
for val in ec2_response['Reservations']:
    for item in val['Instances']:
        print(item['InstanceId'])

ec2_vol_response = ec2_con_cli.describe_volumes()
for value in ec2_vol_response['Volumes']:
    print(value['VolumeId'])
