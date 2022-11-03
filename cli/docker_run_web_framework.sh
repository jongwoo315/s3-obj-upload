docker run \
-d --rm \
-p 5555:8000 \
-v $PWD/.env:/.env \
-v ~/.aws:/root/.aws \
web_f:v1