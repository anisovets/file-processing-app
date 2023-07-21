# Use the official AWS Lambda base image for Python
FROM public.ecr.aws/lambda/python:3.8

# Copy your Python code to the /var/task directory in the container
COPY ../src/file_processing_lambda.py /app/file_processing_lambda.py

# Set the handler for the Lambda function (modify as needed)
CMD ["file_processing_lambda.file_upload_handler"]
