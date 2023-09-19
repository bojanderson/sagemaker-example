FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    build-essential

# Install necessary Python packages
RUN pip install numpy pandas scikit-learn boto3

# Set up the working directory
WORKDIR /opt/ml

# Copy the training script
COPY train.py /opt/ml/train.py

ENTRYPOINT ["python", "/opt/ml/train.py"]
