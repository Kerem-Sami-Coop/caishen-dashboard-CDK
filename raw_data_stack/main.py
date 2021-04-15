from constructs import Construct
from cdktf import App, TerraformStack
from imports.aws import AwsProvider
from imports.terraform_aws_modules.Lambda.aws import TerraformAwsModulesLambdaAws as Lambda


class RawDataStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)
        AwsProvider(self, "Aws",  region="us-east-1")

        Lambda(self, "lambda-test",
               function_name="mock-terraform-func",
               handler="test.lambda_handler",
               runtime="python3.8",
               source_path="../test.py")


if __name__ == "__main__":
    app = App()
    RawDataStack(app, "test-lambda-tf")

    app.synth()
