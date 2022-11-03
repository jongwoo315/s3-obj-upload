from flask import Flask
from .s3_obj_upload.basic.views import basic
from .s3_obj_upload.form_data.views import form_data
from .s3_obj_upload.pre_signed_url.views import pre_signed_url

app = Flask(__name__)

app.register_blueprint(basic)
app.register_blueprint(form_data)
app.register_blueprint(pre_signed_url)

@app.before_request
def before_request():
    return

@app.after_request
def after_request(response):
    print(f'response: {response}')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = ['POST']
    return response

@app.route('/', methods=['GET'])
def main():
    return 'main'
