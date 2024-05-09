from datetime import datetime
import boto3

sqs = boto3.client("sqs")

queue_url = "https://sqs.ap-south-1.amazonaws.com/489791930594/Demo-SQS"

response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=10,
    AttributeNames=["All"],
    MessageAttributeNames=["All"],
    VisibilityTimeout=1,
    WaitTimeSeconds=1
)


if "Messages" in response:
    message_receipt_handles = []
    print("Message(s) Received:")
    for message in response["Messages"]:
        message_receipt_handles.append({
            "Id": message["MessageId"],
            "ReceiptHandle": message["ReceiptHandle"]
        })
        print(message["Body"])
        timestamp = float(message["Attributes"]["SentTimestamp"])
        print(f"-------- Sent On {datetime.fromtimestamp(timestamp/1000)}")

    deletion_success = sqs.delete_message_batch(
        QueueUrl=queue_url, Entries=message_receipt_handles)
    if "Failed" not in deletion_success:
        print("Deleted all messages successfully")
else:
    print("No Messages to poll")
