set -a; source .env; set +a

# docker login
aws ecr get-login-password \
--profile $AWS_PROFILE_NAME --region $AWS_REGION | \
docker login --username AWS --password-stdin $AWS_PROFILE_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# docker push (docker-compose.yml에 image명을 aws ecr명으로 미리 지정했기 때문에 docker tag를 사용할 필요가 없다.)
docker push $AWS_PROFILE_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_WEB_SERVICE:latest
docker push $AWS_PROFILE_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_WEB_FRAMEWORK:latest
