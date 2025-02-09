from aws_cdk import App, Environment
from stack import FastapiServerlessStack

app = App()

env = Environment(
  account="123456789012",
  region="eu-west-1",
)
stack = FastapiServerlessStack(
  app,
  "FastApiSlsCDKStack",
  stack_name="qa-test-lambda",
  env=env
)

app.synth()
