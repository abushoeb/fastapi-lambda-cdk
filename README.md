# FastAPI Lambda CDK Example

A simple Hello World FastAPI application deployed as an AWS Lambda function using AWS CDK.

This project demonstrates how to deploy a FastAPI application as a serverless function on AWS Lambda using AWS CDK for infrastructure as code. The application is exposed through API Gateway and can be accessed via HTTP endpoints.

## Project Structure
```
├── api/ # FastAPI application
│   ├── __init__.py
│   ├── main.py
│   └── requirements.txt
├── cdk/ # CDK infrastructure
│   ├── __init__.py
│   ├── cdk.json
│   ├── cdk.py
│   ├── stack.py
│   └── requirements.txt
├── README.md
```

## Prerequisites
- AWS CLI
- Python 3.11+
- AWS CDK CLI
- Docker (for local development and asset bundling)
- Python package management(i prefer [uv](https://docs.astral.sh/uv/) `brew install uv`)

### Deployment

```bash
$ git clone https://github.com/johnshumon/fastapi-lambda-cdk.git && cd fastapi-lambda-cdk

# Create and activate venv
$ uv venv && source .venv/bin/activate

# confirm that venv python is beiong used
$ which python # should point to  /path/to/fastapi-lambda-cdk/.venv/bin/python

# Install dependencies
$ uv pip install -r ./api/requirements.txt
$ uv pip install -r ./cdk/requirements.txt

# Deploy to AWS
$ cd cdk
$ cdk list
$ cdk synth
$ cdk deploy
```

The deployment will output the API Gateway URL where your FastAPI application can be accessed e.g.: `https://<redacted>.execute-api.eu-west-1.amazonaws.com`
