FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    build-essential

# Install necessary Python packages
RUN pip install numpy pandas scikit-learn boto3

# Sets up the environment and runs your code
ENV PYTHONUNBUFFERED=TRUE
ENTRYPOINT ["python3"]
