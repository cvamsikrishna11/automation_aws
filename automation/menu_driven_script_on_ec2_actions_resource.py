import boto3
import sys

aws_mag_con = boto3.session.Session(profile_name='vamsi', region_name='ap-south-east-1')
ec2_con_cli = aws_mag_con.client(service_name='ec2', region_name='ap-south-east-1')
ec2_con_re = aws_mag_con.resource(service_name='ec2', region_name='ap-southeast-1')

while True:
    print('''
    This script performs the following actions on ec2 instances
    ''')
    print('''
    1. Start
    2. Stop
    3. Terminate
    4. Exit
    ''')
    opt = int(input('Enter your option: '))
    if opt == 1:
        instance_id = input('Enter your instance ID: ')
        my_instance_obj = ec2_con_re.Instance(instance_id)
        # print(dir(my_instance_obj))
        print('Starting EC2 instance...')
        my_instance_obj.start()
    elif opt == 2:
        instance_id = input('Enter your instance ID: ')
        my_instance_obj = ec2_con_re.Instance(instance_id)
        # print(dir(my_instance_obj))
        print('Stopping EC2 instance...')
        my_instance_obj.stop()
    elif opt == 3:
        instance_id = input('Enter your instance ID: ')
        my_instance_obj = ec2_con_re.Instance(instance_id)
        print('Terminating the EC2 instance...')
        my_instance_obj.terminate()
    elif opt == 4:
        print('Thanks for using...')
        sys.exit()
    else:
        print('Option invalid, please try again!')
