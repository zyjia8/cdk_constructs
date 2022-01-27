from constructs import Construct
from aws_cdk import (
    # Duration,
    # Stack,
    aws_sqs as sqs,
)
class MyConstructQueue(Construct):

    def __init__(self, scope: Construct, id: str, queue_name: str):
        super().__init__(scope, id)
        self.queue = sqs.CfnQueue(self, queue_name,
            content_based_deduplication=False,
            fifo_queue=False,
            queue_name=queue_name
        )

  