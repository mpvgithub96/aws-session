import sys
import boto3

sqs = boto3.client("sqs")

queue_url = "https://sqs.ap-south-1.amazonaws.com/489791930594/Demo-SQS"

response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        "Title": {
            "DataType": "String",
            "StringValue": "The Whistler"
        },
        "Author": {
            "DataType": "String",
            "StringValue": "Manjunath PV"
        },
        "WeeksOn": {
            "DataType": "Number",
            "StringValue": "6"
        }
    },
    MessageBody=(sys.argv[1])
)


message_id = response["MessageId"]
print(
    f"The message has been sent successfully. The message ID is {message_id}")
