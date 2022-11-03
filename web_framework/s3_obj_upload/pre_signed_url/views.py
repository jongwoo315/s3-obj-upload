import os
from dotenv import load_dotenv
from flask import Blueprint, request
import requests
from web_framework.helper.common import load_s3_client

load_dotenv()

pre_signed_url = Blueprint(
    name='pre_signed_url',
    import_name=__name__,
    url_prefix='/upload_file'
)

@pre_signed_url.route('/pre_signed_url', methods=['POST'])
def upload_file_pre_signed_url():
    """
    curl -v -X POST \
    -H 'Content-Type: multipart/form-data' \
    --url http://127.0.0.1:5555/upload_file/pre_signed_url \
    -F 'test_file=@/Users/jw/Downloads/asdf.pdf'
    """
    print(request.headers)

    file_name = request.files.get('test_file').filename
    file = request.files.get('test_file')

    s3_client = load_s3_client()
    presigned_post = s3_client.generate_presigned_post(
        Bucket=os.getenv('S3_BUCKET'),
        Key=file_name,
        Fields=None,
        Conditions=None,
        ExpiresIn=3600
    )

    with requests.Session() as req_session:
        req_session.post(
            url=presigned_post.get('url'),
            data={
                'key': presigned_post.get('fields').get('key'),
                'policy': presigned_post.get('fields').get('policy'),
                'x-amz-algorithm': presigned_post.get('fields').get('x-amz-algorithm'),
                'x-amz-credential': presigned_post.get('fields').get('x-amz-credential'),
                'x-amz-date': presigned_post.get('fields').get('x-amz-date'),
                'x-amz-signature': presigned_post.get('fields').get('x-amz-signature'),
            },
            files={
                'file': file.read()
            }
        )

    return 'file_pre_signed_url uploaded'
