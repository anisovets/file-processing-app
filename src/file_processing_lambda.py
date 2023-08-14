import boto3
import logging

def file_upload_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info('Lambda function has been triggered!')

    s3Client = boto3.client('s3')

    
    return "File processing handler!"