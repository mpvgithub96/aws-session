from api.settings import Settings
import boto3


class SQS:
    def __init__(self):
        config = Settings()
        self.queue_url = config.QUEUE_URL
        self.client = boto3.client("sqs")

    def send(self, message: str, delay_seconds: int = 0):
        response = self.client.send_message(
            QueueUrl=self.queue_url,
            DelaySeconds=delay_seconds,
            MessageBody=message
        )
        if "MessageId" in response:
            return {
                "status": "success",
                "message_id": response["MessageId"]
            }
        return {
            "status": "Failed"
        }

    def receive(self):
        response = self.client.receive_message(
            QueueUrl=self.queue_url,
            MaxNumberOfMessages=10,
            AttributeNames=["All"],
            MessageAttributeNames=["All"],
            VisibilityTimeout=30,
            WaitTimeSeconds=5
        )

        if "Messages" in response:
            for message in response["Messages"]:
                return {
                    "message_id": message["MessageId"],
                    "message_body": message["Body"],
                    "receipt_handle": message["ReceiptHandle"],
                }
        return "No Messages To Retrieve"

    def delete(self, receipt_handle: str):
        response = self.client.delete_message(
            QueueUrl=self.queue_url,
            ReceiptHandle=receipt_handle
        )
        return response


class SNS:
    def __init__(self):
        config = Settings()
        self.topic_arn = config.TOPIC_ARN
        self.client = boto3.client("sns")

    def publish(self, message: str):
        response = self.client.publish(
            TopicArn=self.topic_arn,
            Message=message
        )
        return response
