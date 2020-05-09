import boto3

aws_profile = boto3.session.Session(profile_name='vamsi')

s3_resource = aws_profile.resource(service_name='s3', region_name='ap-southeast-1')

bucket_name = 'elktests3logs'
bucket_obj = s3_resource.Bucket(bucket_name)
counter = 0
# for each_obj in bucket_obj.objects.all():
#     counter +=1
#     print(each_obj)
# print(counter)


s3_client = aws_profile.client(service_name='s3', region_name='ap-southeast-1')
paginator = s3_client.get_paginator('list_objects')

for each_page in paginator.paginate(Bucket=bucket_name):
    for each_obj in each_page['Contents']:
        counter += 1
        print(each_obj['Key'])
print(counter)

# for each_obj in s3_client.list_objects(Bucket=bucket_name)['Contents']:
#     counter +=1
#     print(each_obj['Key'])
# print(counter)
