import boto3

aws_profile = boto3.session.Session(profile_name='vamsi')
s3_resource = aws_profile.resource(service_name='s3', region_name='ap-southeast-1')
s3_client = aws_profile.client(service_name='s3', region_name='ap-southeast-1')

print('*******************Through resource****************')
bucket_count = 0
for each_bucket in s3_resource.buckets.all():
    bucket_count += 1
    print(each_bucket.name)
print(bucket_count)

counter = 0
print('*******************Through client****************')
for each_bucket in s3_client.list_buckets()['Buckets']:
    counter += 1
    print(each_bucket)
print(counter)
