# Use the official AWS Lambda base image for Python
FROM public.ecr.aws/lambda/python:latest
MAINTAINER Yaru Anisovec

# Copy your Python code to the /var/task directory in the container
COPY ./src/file_processing_lambda.py /var/task/file_processing_lambda.py
COPY ./src/requirements.txt //var/task/requirements.txt

WORKDIR /var/task


RUN python3 -m pip install -r requirements.txt

# Set the handler for the Lambda function (modify as needed)
CMD ["file_processing_lambda.file_upload_handler"]