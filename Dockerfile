# Use the official AWS Lambda base image for Python
FROM public.ecr.aws/lambda/python:latest

# Copy your Python code to the /var/task directory in the container
#COPY ./src/file_processing_lambda.py /app/
COPY ./src/file_processing_lambda.py /src/file_processing_lambda.py
COPY ./src/requirements.txt /src/requirements.txt

WORKDIR /src


RUN python3 -m pip install -r requirements.txt

# Set the handler for the Lambda function (modify as needed)
CMD ["file_processing_lambda.file_upload_handler"]