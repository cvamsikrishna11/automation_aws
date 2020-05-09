import boto3

aws_profile = boto3.session.Session(profile_name='vamsi')

iam_resource = aws_profile.resource(service_name='iam')
count = 0
# for each_user in iam_resource.users.all():
#     count += 1
#     print(each_user, count)

iam_client = aws_profile.client(service_name='iam')
for each_user in iam_client.list_users()['Users']:
    count += 1
    print(each_user['UserName'], count)

paginator = iam_client.get_paginator('list_users')
print('*********paginator***********')
# response_iterator = paginator.paginate(
#     PathPrefix='string',
#     PaginationConfig={
#         'MaxItems': 123,
#         'PageSize': 123,
#         'StartingToken': 'string'
#     }
# )
count_paginator = 0
for each_page in paginator.paginate():
    for each_user in each_page['Users']:
        count_paginator += 1
        print(each_user['UserName'])
print(count_paginator)

#########################################
# Paginator for S3
