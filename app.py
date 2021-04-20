from aws_cdk import core
from pipeline.raw_data import RawDataStack

app = core.App()
RawDataStack(app, "test-deployment")
app.synth()
