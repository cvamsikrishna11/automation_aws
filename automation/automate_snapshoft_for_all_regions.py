import boto3

aws_profile = boto3.session.Session(profile_name='vamsi')
ec2_client = aws_profile.client(service_name='ec2', region_name='ap-southeast-1')

all_regions = []
for each_region in ec2_client.describe_regions()['Regions']:
    all_regions.append(each_region['RegionName'])

for each_region in all_regions:
    print('working on...', each_region)
    ec2_client = aws_profile.client(service_name='ec2', region_name=each_region)
    filter_for_volume_using_tags = {"Name": "tag:name", "Values": ["testing backup vol"]}
    list_of_volids = []
    # for each_vol in ec2_client.describe_volumes(Filters=[filter_for_volume_using_tags])['Volumes']:
    #     list_of_volids.append(each_vol['VolumeId'])
    # print(list_of_volids)
    paginator = ec2_client.get_paginator('describe_volumes')
    for each_page in paginator.paginate(Filters=[filter_for_volume_using_tags]):
        for each_vol in each_page['Volumes']:
            list_of_volids.append(each_vol['VolumeId'])
    print(list_of_volids)
    if bool(list_of_volids) == False:
        continue
    snapshot_id = []
    for each_vol_id in list_of_volids:
        print('Taking snap of volume: ', each_vol_id)
        res = ec2_client.create_snapshot(Description='Taking snap with Lambda and CloudWatch', VolumeId=each_vol_id,
                                         TagSpecifications=[{
                                             'ResourceType': 'snapshot',
                                             'Tags': [{
                                                 'Key': 'Delete-on',
                                                 'Value': '90'
                                             },
                                                 {
                                                     'Key': 'backup',
                                                     'Value': 'yes'
                                                 }
                                             ]
                                         }
                                         ]
                                         )
        snapshot_id.append(res.get('SnapshotId'))
    print('snpashot id are:', snapshot_id)
    waiter = ec2_client.get_waiter('snapshot_completed')
    waiter.wait(SnapshotIds=snapshot_id)
    print('Successfully completed snaps for the volumes of', list_of_volids)
