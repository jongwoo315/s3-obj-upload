import os
from dotenv import load_dotenv
from flask import Blueprint, request
from web_framework.helper.common import load_s3_client

load_dotenv()

form_data = Blueprint(
    name='form_data',
    import_name=__name__,
    url_prefix='/upload_file'
)

@form_data.route('/form_data', methods=['POST'])
def upload_file_form_data():
    """
    curl -v -X POST \
    -H 'Content-Type: multipart/form-data' \
    --url http://127.0.0.1:5555/upload_file/form_data \
    -F 'name=jw' \
    -F 'days={\"mon\":123}' \
    -F 'test_jpg=@/Users/jw/Downloads/IMG_3158.JPG' \
    -F 'test_pdf=@/Users/jw/Downloads/data-engineering-with-python.pdf'
    """
    # print(request.headers)

    # print(request.form)  # form_data (파일이 아닌 것들)
    # print(request.files)  # form_data (파일)
    # print(request.files.items())  # form_data (파일, generator(모든 파일을 순회할 때))

    s3_client = load_s3_client()

    # 업로드할 파일이 하나일 때
    # result = s3_client.put_object(
    #     Bucket=os.getenv('S3_BUCKET),
    #     Key=request.files.get('test_jpg').filename,
    #     Body=request.files.get('test_jpg')
    # )

    # 업로드할 파일이 여러개일 때
    for _, file_info in request.files.items():
        s3_client.put_object(
            Bucket=os.getenv('S3_BUCKET'),
            Key=file_info.filename,
            Body=file_info
        )

    return 'file_form_data uploaded'
