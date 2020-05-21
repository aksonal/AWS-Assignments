#Create a lambda function to send an email notification to your email id of your AWS account, as soon as you delete a file from an S3 bucket,
#mentioning the file name which is deleted.

import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    
    #event variable is a dictionary we will be getting
    for i in event["Records"]:
        action = i["eventName"] #this will tell us what action we have performed deletion/creation
        ip = i["requestParameters"]["sourceIPAddress"] # to know who has performed this action
        bucket_name = i["s3"]["bucket"]["name"] #bucket name
        object = i["s3"]["object"]["key"] #name of the object/file name
        
    client = boto3.client("ses")  #boto 3 object for SES service
    
    #info needed to send email/ email contents
    
    subject = str(action) + 'Event from '+ bucket_name # it tells subject line as object removed/created event from bucket_name
    
    #body- we can define body in simple text format or use html
    body = """
           <br>
           This mail is to notify you regarding {} event
           Source IP: {}
           And the file deleted is {} from bucket {}
    
    """.format(action,ip,object,bucket_name)
    
    #combine this into dictionary
    message = {"Subject": {"Data":subject},"Body":{"Html": {"Data":body}}} #if we had not used html,instead used text we would write text there in place of html
    
    #send emial
    #we need to define 3 parameters source-who will send the email , destination- to whom you want to send the email and message-your message
    response = client.send_email(Source = "sonal.kumar98@gmail.com",Destination = {"ToAddresses": ["sonal.kumar98@gmail.com"]},Message = message)
    
        
    
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
