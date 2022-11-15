# s3-obj-upload
Nginx, Flask, Boto3 library를 사용하여 파일을 s3 bucket에 업로드하는 프로젝트

## Table of Contents
- [Introduction](#Introduction)
- [Technologies Used](#Technologies-Used)
- [Setup](#Setup)
- [Usage](#Usage)
- [Acknowledgements](#Acknowledgements)

## Introduction
- Docker Compose를 활용한 Nginx, Flask 서비스 구현 및 AWS까지 배포하는 것이 주 목적
- Flask blueprint로 기능별로 함수(api) 분리
- AWS S3 bucket에 업로드는 boto3 library사용
- docker context를 사용해 aws에 배포
    - cloudformation stack 자동 생성 (ecs 관련 인프라)
    - custom 인프라를 사용하고자 하는 경우 `docker-compose.yml`에 `x-aws-cloudformation` key하위에 cloudformation resource 추가 필요

## Technologies Used
- Python: 3.9
- Flask
- Nginx
- Docker
- Docker Compose

## Setup
- `.env.default`
    - aws 관련 설정값 입력 후, `.env`로 파일명 수정 
    - `LOAD_BALANCER_DNS`는 ecs로 docker push 후 확인가능
- 인프라 설정
    - `$ cdk deploy <stack명>`
    - s3 bucket, ecr repository
    - 별도 git 프로젝트([iac-aws-cdk](https://bit.ly/3X3MDk9))에서 aws-cdk를 사용해 배포
- 설정 및 배포
    ```shell
    $ cd web_framework
    $ pipenv shell --python 3.9
    $ python -V
    $ pipenv install

    $ cli/docker_push.sh
    $ docker context create ecs <컨텍스트명>  # AWS environment variables 선택
    $ docker context use <컨텍스트명>

    $ export AWS_ACCESS_KEY_ID=<아이디>
    $ export AWS_SECRET_ACCESS_KEY=<시크릿>
    $ export AWS_DEFAULT_REGION=<리전>

    $ docker-compose up
    ```
- source 업데이트시
    ```shell
    $ docker context use default
    $ docker-compose up -d --force-recreate --build
    $ docker context use <컨텍스트명>
    $ docker-compose up  # shell에서 진행상황 확인되지 않는다
    ```
- 종료
    ```shell
    $ docker context use default
    $ docker-compose down  # 로컬이라면 docker-compose stop도 가능
    ```

## Usage
- Local Test
    ```shell
    $ docker context show  # default 확인
    $ docker-compose up -d  # 로컬 테스트 (docker-compose.yml ~/.aws bind 주석해제)
    $ docker_compose_s3_obj_upload.sh  # 각자의 로컬에 위치한 파일명으로 변경
    ```
    - 웹브라우저에서 http://127.0.0.1:80 접속이 되는지 확인
- Service Check
    - `.env`에 `LOAD_BALANCER_DNS`값 추가
   ```shell
   $ cli/aws_ecs_s3_obj_upload.sh
   ``` 

## Acknowledgements
- https://www.patricksoftwareblog.com/how-to-use-docker-and-docker-compose-to-create-a-flask-application/
- https://gitlab.com/patkennedy79/flask_recipe_app/-/tree/master/
- https://stackoverflow.com/questions/69325960/docker-breaks-when-trying-to-use-created-aws-context
- https://docs.docker.com/cloud/ecs-integration/#tuning-the-cloudformation-template
- https://github.com/docker/compose-cli/issues/1537
- https://stackoverflow.com/questions/30269672/unable-to-use-lt-when-running-nginx-docker-or-cat-logs
- https://serverfault.com/questions/814767/413-request-entity-too-large-in-nginx-with-client-max-body-size-set
