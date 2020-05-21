#lambda function to terminate EC2 Instance

import boto3

region = 'ap-south-1'
instances = ['i-0983c7133022bd164']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    
    #terminate EC2 Instance
    ec2.terminate_instances(InstanceIds=instances)
    print('Terminated your instance: ' + str(instances))
    
  

