import os
from dotenv import load_dotenv
from flask import Blueprint, request
from web_framework.helper.common import load_s3_client

load_dotenv()

basic = Blueprint(
    name='basic',
    import_name=__name__,
    url_prefix='/upload_file'
)

@basic.route('/basic', methods=['POST'])
def upload_file_basic():
    """
    curl -v -X POST \
    -H 'Content-Type: application/jpg' \
    --url http://127.0.0.1:5555/upload_file/basic?filename=qwer.jpg \
    --data-binary '@/Users/jw/Downloads/IMG_3158.JPG'
    """
    # print(request.headers)

    query_string = request.args.to_dict()
    body_data = request.data
    # print(f'query_string: {query_string}')
    # print(f'body_data: {body_data}')  # body (binary data)

    s3_client = load_s3_client()
    s3_client.put_object(
        Bucket=os.getenv('S3_BUCKET'),
        Key=query_string.get('filename'),
        # Body=base64.b64decode(body_data)  # 불필요
        Body=body_data
    )

    return 'file_basic uploaded' 
