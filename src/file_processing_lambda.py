import boto3
import logging
import os

def file_upload_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.debug('Lambda function has been triggered!')
    print('## ENVIRONMENT VARIABLES')
    print(os.environ['AWS_LAMBDA_LOG_GROUP_NAME'])
    print(os.environ['AWS_LAMBDA_LOG_STREAM_NAME'])
    print('## EVENT')

    s3Client = boto3.client('s3')
    sqsClient = boto3.client('sqs')

    queue_url = sqsClient.get_queue_url(QueueName='image-processing-queue')['QueueUrl']
    sqsClient.send_message(
        QueueUrl=queue_url,
        MessageBody='Message from Lambda!'
    )


    
    return "File processing handler! 256 "+os.environ['AWS_LAMBDA_LOG_GROUP_NAME']