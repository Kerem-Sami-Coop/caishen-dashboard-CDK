from constructs import Construct
from cdktf import App, TerraformStack
from imports.aws import SnsTopic, AwsProvider
from imports.terraform_aws_modules.vpc.aws import TerraformAwsModulesVpcAws as Vpc
import yaml
import os

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)
        AwsProvider(self, 'Aws',  region='us-west-2')

        Vpc(self, 'CustomVpc',
        name='custom-vpc',
        cidr='10.0.0.0/16',
        azs=["us-east-1a", "us-east-1b"],
        public_subnets=["10.0.1.0/24", "10.0.2.0/24"]
        )
        #SnsTopic(self, 'Topic', display_name='my-first-sns-topic')


if __name__ == "__main__":
    with open("secrets.yaml", "r") as f:
        config = yaml.safe_load(f)
    for key in config.keys():
        os.environ[key] = config[key]

    app = App()
    MyStack(app, "python-aws")

    app.synth()