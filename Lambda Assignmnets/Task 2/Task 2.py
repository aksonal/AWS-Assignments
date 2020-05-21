#When you terminate an EC2 instance, a snapshot should be created from the EBS volume attached to the EC2 instance automatically and store it 
#in an S3 bucket. Create a lambda function to automate the above.

import json
import boto3

region = 'ap-south-1'
az = 'ap-south-1a'
vpc = 'vpc-d24648ba'
subnet = 'subnet-5f95a137'
Volume_ID = 'vol-0717345ff4b5f9b4d'

def lambda_handler(event, context):
    # TODO implement
    
    client = boto3.client('ec2',region)
    s3 = boto3.client('s3')
   
    response = client.create_snapshot(
    Description='Create a snapshot of this instance',
    VolumeId=Volume_ID)
    print('SnapShot Created')
    
    #print dictionary that contains info abt the snapshot created
    print (response)
    
    #upload snapshot created to s3 bucket
    s3.put_object(Bucket="abracadabra11", Key = "snapshot.txt", Body = str(response))
