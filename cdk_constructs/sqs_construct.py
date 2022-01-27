from constructs import Construct
from aws_cdk import (
    # Duration,
    # Stack,
    aws_sqs as sqs,
)
class MyConstructQueue(Construct):

    def __init__(self, scope: Construct, id: str, queue_name: str):
        super().__init__(scope, id)
        self.queue = sqs.Queue(self, queue_name)
  