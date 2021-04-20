from aws_cdk import core
from aws_cdk.aws_s3 import Bucket
from aws_cdk.aws_lambda import Function, Runtime, Code


class RawDataStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str):
        super().__init__(scope, id)

        raw_bucket = Bucket(self, "raw-data-stack-1",
                            bucket_name="caishen-raw-data-dev")

        handler = Function(self, "test-lambda",
                           runtime=Runtime.PYTHON_3_8,
                           code=Code.from_asset("./pipeline/export.zip"),
                           handler="test.lambda_handler",
                           environment={
                               "BUCKET": raw_bucket.bucket_name
                           }
                           )

        raw_bucket.grant_read_write(handler)
