import boto3

aws_mag_con = boto3.session.Session(profile_name='vamsi')

'''
With Resource
'''
ec2_con_re = aws_mag_con.resource(service_name='ec2', region_name='ap-southeast-1')

f_ebs_un_used = {'Name': 'status', 'Values': ['available']}
for each_vol in ec2_con_re.volumes.filter(Filters=[f_ebs_un_used]):
    if not each_vol.tags:
        print(each_vol.id, each_vol.state, each_vol.tags)
        print('Deleting unused and and untagged objects...')
        each_vol.delete()
print('Deleted all unused and untagged volumes..')

'''
With Client
'''
ec2_con_cli = aws_mag_con.client(service_name='ec2', region_name='ap-southeast-1')

for each_item in ec2_con_cli.describe_volumes()['Volumes']:
    if not "Tags" in each_item and each_item['State'] == 'available':
        print('Deleting..', each_item['VolumeId'])
        ec2_con_cli.delete_volume(VolumeId=each_item['VolumeId'])
print('Delete all unused and untagged volumes..')
