import boto3
import time

aws_con = boto3.session.Session(profile_name='vamsi')
ec2_con_cli = aws_con.client(service_name='ec2', region_name='ap-southeast-1')
ec2_con_re = aws_con.resource(service_name='ec2', region_name='ap-southeast-1')

'''
With resource object
'''

my_instance_obj = ec2_con_re.Instance('i-0a92d5196bee0334c')
print('Starting given instance...')
my_instance_obj.start()
'''loop iterates for 40 times, with 5 sec duration, total waits for 200 seconds, if instance is not created in the
meantime then the function will throw an exception '''
my_instance_obj.wait_until_running()
print('Instance status is...', my_instance_obj.state['Name'])

'''
wWth client object
'''
print('Starting the given instance...')
ec2_response = ec2_con_cli.start_instances(InstanceIds=['i-0a92d5196bee0334c'])
waiter = ec2_con_cli.get_waiter('instance_running')
'''
40 checks after every 15 sec, 600 sec, good to use waiter from Client Obj
'''
waiter.wait(InstanceIds=['i-0a92d5196bee0334c'])
print('Instance is running...')

'''
Start EC2 with Resource Obj and Wait with Client obj
'''
my_instance_obj = ec2_con_re.Instance('i-0a92d5196bee0334c')
print('Starting given instance...')
my_instance_obj.start()
waiter = ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-0a92d5196bee0334c'])
print('Instance is running...')

'''
Custom logic for wait
'''
while True:
    my_instance_obj = ec2_con_re.Instance('i-0a92d5196bee0334c')
    print('Current status of ec2 is: ', my_instance_obj.state['Name'])
    if my_instance_obj.state['Name'] == 'running':
        break
    print('Waiting to get running status...')
    time.sleep(5)
    print('Now your instance is up and running...')
