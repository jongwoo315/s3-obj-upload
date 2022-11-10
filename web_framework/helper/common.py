import os
import boto3
from dotenv import load_dotenv

load_dotenv()

def load_s3_client():
    try:
        aws_env = os.environ['AWS_EXECUTION_ENV']
        print(f'aws_env: {aws_env}')
    except KeyError:
        print('local env')
        boto3_session = boto3.Session(
            profile_name=os.getenv('AWS_PROFILE'),
            region_name=os.getenv('AWS_REGION')
        )
    else:
        print('aws env')
        boto3_session = boto3.Session()

    boto3_session = boto3.Session()

    s3_client = boto3_session.client(service_name='s3') 

    return s3_client
