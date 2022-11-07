FROM python:3.9-slim

WORKDIR /src

# localhost 테스트
# COPY /web_framework /src/web_framework/

# docker-compose build시 해당 Dockerfile이 root dir
COPY . /src/web_framework/

RUN pip install -r web_framework/requirements.txt 

ENV FLASK_APP=web_framework

# CMD [ "flask", "run", "-h", "0.0.0.0", "-p", "8000" ]
CMD [ "gunicorn", "-w", "2", "-b", ":8000", "web_framework:app" ]