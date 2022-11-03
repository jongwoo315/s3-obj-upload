import os
import boto3
from dotenv import load_dotenv

load_dotenv()

def load_s3_client():
    boto3_session = boto3.Session(
        profile_name=os.getenv('AWS_PROFILE'),
        region_name=os.getenv('AWS_REGION')
    )
    s3_client = boto3_session.client(service_name='s3')
    return s3_client
