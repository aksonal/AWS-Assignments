# lambda function to stop EC2 instance

import boto3

region = 'ap-south-1'
instances = ['i-0983c7133022bd164']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    
    #Stop EC2 Instance
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instance: ' + str(instances))
    
    
