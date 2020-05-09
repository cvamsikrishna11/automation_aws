import boto3

aws_mag_con = boto3.session.Session(profile_name='vamsi')
ec2_con_re = aws_mag_con.resource(service_name='ec2', region_name='us-east-1')
ec2_con_cli = aws_mag_con.client(service_name='ec2', region_name='us-east-1')

print('*********all******************')
for each in ec2_con_re.instances.all():
    print(each)
print('****************limit*********')
for each in ec2_con_re.instances.limit(5):
    print(each)

print('**********filter**************')
f1 = {'Name': 'instance-state-name', 'Values': ['running', 'stopped']}
f2 = {'Name': 'instance-type', 'Values': ['t2.micro']}
for each in ec2_con_re.instances.filter(Filters=[f1, f2]):
    print(each)

# print('****Starting all instances****')
# instance_list = []
# for each in ec2_con_re.instances.all():
#     instance_list.append(each.id)
# print(instance_list)
# ec2_con_re.instances.start()
# waiter = ec2_con_cli.get_waiter('instance_running')
# waiter.wait(InstanceIds=instance_list)
# print('All instances are up and running...')

print('****Starting filtered instances****')
instance_list = []
for each in ec2_con_re.instances.filter():
    instance_list.append(each.id)
print(instance_list)
ec2_con_re.instances.start()
waiter = ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=instance_list)
print('All instances are up and running...')
