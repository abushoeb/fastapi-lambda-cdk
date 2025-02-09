# FastAPI Lambda CDK Example

A simple Hello World FastAPI application deployed as an AWS Lambda function using AWS CDK.

This project demonstrates how to deploy a FastAPI application as a serverless function on AWS Lambda using AWS CDK for infrastructure as code. The application is exposed through API Gateway and can be accessed via HTTP endpoints.

## Project Structure
```
.
├── cdk
│   ├── Pipfile
│   ├── api
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── requirements.txt
│   └── cdk
│       ├── __init__.py
│       ├── cdk.json
│       ├── cdk.py
│       ├── requirements.txt
│       └── stack.py
├── serverless
│   ├── app.py
│   ├── package.json
│   ├── requirements.txt
│   └── serverless.yml
├── .gitignore
└── README.md
```

## Prerequisites
- AWS CLI
- Python 3.11+
- AWS CDK CLI
- Docker (for local development and asset bundling)
- Python package management(pipenv (`brew install pipenv`) or uv (`brew install uv`))

### Deployment using CDK

```bash
$ git clone https://github.com/johnshumon/fastapi-lambda-cdk.git && cd fastapi-lambda-cdk/cdk

# Create and activate venv
$ pipenv shell

# confirm that venv python is beiong used
$ which python # should point to  /path/to/fastapi-lambda-cdk/.venv/bin/python

# Install dependencies
$ pipenv install
$ pip install -r ./api/requirements.txt --platform linux_x86_64 --target ./python --only-binary=:all:
$ pip install -r ./cdk/requirements.txt --platform linux_x86_64 --target ./python --only-binary=:all:

# Deploy to AWS
$ cd cdk
$ cdk list
$ cdk synth
$ cdk deploy
```

### Deployment using Serverless

```bash
$ git clone https://github.com/johnshumon/fastapi-lambda-cdk.git && cd fastapi-lambda-cdk/serverless

# Create and activate venv
$ pipenv shell

# confirm that venv python is beiong used
$ pnpm install

# export aws credentials as environment variables
# becuase serverless got issue picking up SSO credentials or
# SSO profile e.g. sls deploy --aws-profile <profile-name>
$ export AWS_ACCESS_KEY_ID=<key>
$ export AWS_SECRET_ACCESS_KEY=<secret>
$ export AWS_SESSION_TOKEN=<token>

# Install dependencies
$ sls deploy
```

Either deployment should export the URL where your FastAPI application can be accessed e.g.: `https://<redacted>.execute-api.eu-west-1.amazonaws.com`
