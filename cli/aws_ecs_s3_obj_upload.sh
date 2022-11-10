set -a; source .env; set +a;

# curl -v -X POST \
# -H 'Content-Type: application/jpg' \
# --url $LOAD_BALANCER_DNS:80/upload_file/basic?filename=qwer.jpg \
# --data-binary '@/Users/jw/Downloads/IMG_3158.JPG'

curl -v -X POST \
-H 'Content-Type: multipart/form-data' \
--url $LOAD_BALANCER_DNS:80/upload_file/form_data \
-F 'name=jw' \
-F 'days={\"mon\":123}' \
-F 'test_jpg=@/Users/jw/Downloads/IMG_3158.JPG' \
-F 'test_pdf=@/Users/jw/Downloads/data-engineering-with-python.pdf'

# curl -v -X POST \
# -H 'Content-Type: multipart/form-data' \
# --url $LOAD_BALANCER_DNS:80/upload_file/pre_signed_url \
# -F 'test_file=@/Users/jw/Downloads/asdf.pdf' 

