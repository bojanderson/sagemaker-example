# README

This assumes you are in this directory when running these commands in Windows command prompt. This assumes you are using us-east-2 and your Account ID is 987987637308

```{bash}
docker build -t my-image .

aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 987987637308.dkr.ecr.us-east-2.amazonaws.com

aws ecr create-repository --repository-name sagemaker-example

docker tag my-image:latest 987987637308.dkr.ecr.us-east-2.amazonaws.com/sagemaker-example:latest

docker push 987987637308.dkr.ecr.us-east-2.amazonaws.com/sagemaker-example:latest
```

The URI for the ECR image is used in the code later.
