from constructs import Construct
from cdktf import App, TerraformStack
from imports.aws import AwsProvider
from imports.terraform_aws_modules.s3_bucket.aws import TerraformAwsModulesS3BucketAws as S3Bucket
import yaml
import os


class RawDataStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)
        AwsProvider(self, "Aws",  region="us-east-1")

        S3Bucket(self,"raw-data-bucket",
                  acl="private")


class ArtifactsStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)
        AwsProvider(self, "Aws",  region="us-east-1")

        S3Bucket(self,"artifacts-bucket",
                  acl="private")


if __name__ == "__main__":
    with open("secrets.yaml", "r") as f:
        config = yaml.safe_load(f)
    for key in config.keys():
        os.environ[key] = config[key]

    app = App()
    RawDataStack(app, "raw-data-stack")
    ArtifactsStack(app, "artifacts-stack")

    app.synth()