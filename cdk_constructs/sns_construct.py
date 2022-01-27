from constructs import Construct
from aws_cdk import (
    # Duration,
    # Stack,
    aws_sns as sns,
)
class NotifyingTopic(Construct):

    def __init__(self, scope: Construct, id: str, tname: str):
        super().__init__(scope, id)
        self.topic = sns.CfnTopic(self, tname,
            content_based_deduplication=False,
            display_name=tname,
            fifo_topic=False,
            topic_name=tname
        )
  