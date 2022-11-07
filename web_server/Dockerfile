FROM nginx:1.11.3

RUN rm \
/etc/nginx/nginx.conf \
/etc/nginx/conf.d/default.conf

# localhost 테스트
# COPY /web_server/nginx.conf /etc/nginx/
# COPY /web_server/s3_obj_upload.conf /etc/nginx/conf.d/

# docker-compose build시 해당 Dockerfile이 root dir
COPY /nginx.conf /etc/nginx/
COPY /s3_obj_upload.conf /etc/nginx/conf.d/

CMD [ "nginx", "-g", "daemon off;" ]