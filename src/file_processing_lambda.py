import boto3
import logging

def file_upload_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.debug('Lambda function has been triggered!')

    s3Client = boto3.client('s3')
    sqsClient = boto3.client('sqs')

    queue_url = sqsClient.get_queue_url(QueueName='image-processing-queue')['QueueUrl']
    sqsClient.send_message(
        QueueUrl=queue_url,
        MessageBody='Message from Lambda!'
    )


    
    return "File processing handler!"