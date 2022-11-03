FROM nginx:1.11.3

RUN rm \
/etc/nginx/nginx.conf \
/etc/nginx/conf.d/default.conf

COPY /web_server/nginx.conf /etc/nginx/
COPY /web_server/s3_obj_upload.conf /etc/nginx/conf.d/

CMD [ "nginx", "-g", "daemon off;" ]