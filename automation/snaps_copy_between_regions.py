import os, sys
from pprint import pprint

try:
    import boto3

    print('Imported boto3 successfully...')
except Exception as e:
    print(e)
    sys.exit(1)
source_region = 'ap-southeast-1'
dest_rgion = 'us-east-2'

aws_profile = boto3.session.Session(profile_name='vamsi')
ec2_source_client = aws_profile.client(service_name='ec2', region_name=source_region)
sts_client = aws_profile.client(service_name='sts', region_name=source_region)
account_id = sts_client.get_caller_identity().get('Account')
bkp_snaps = []
f_bkp = {'Name': "tag:backup", "Values": ['yes']}
for each_snap in ec2_source_client.describe_snapshots(OwnerIds=[account_id], Filters=[f_bkp]).get('Snapshots'):
    bkp_snaps.append(each_snap.get('SnapshotId'))
print(bkp_snaps)
#
ec2_dest_client = aws_profile.client(service_name='ec2', region_name=dest_rgion)
for each_source_snap_id in bkp_snaps:
    print('Taking backup for id of {} into a {}'.format(each_source_snap_id, dest_rgion))
    ec2_dest_client.copy_snapshot(Description='Copying snapshot from one region to another region',
                                  SourceRegion=source_region, SourceSnapshotId=each_source_snap_id)
print("EBS snapshot copy to destination region is completed")
print('Modifying tags for the snapshots for which backup is completed')
for each_source_snap_id in bkp_snaps:
    print('Deleting old tags for...', each_source_snap_id)
    ec2_source_client.delete_tags(
        Resources=[each_source_snap_id],
        Tags=[{
            'Key': 'backup',
            'Value': 'yes'
        }

        ]
    )
    print('creating new tags for...', each_source_snap_id)
    ec2_source_client.create_tags(
        Resources=[each_source_snap_id],
        Tags=[{
            'Key': 'backup',
            'Value': 'completed'
        }

        ]
    )
