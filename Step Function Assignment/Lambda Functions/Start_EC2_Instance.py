#lambda function to start EC2 

import boto3

region = 'ap-south-1'
instances = ['i-0983c7133022bd164']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    
    #start EC2 Instance
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))
        
