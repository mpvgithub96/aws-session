from fastapi import FastAPI
from api.models import SendMessageRequest, DeleteMessageRequest
from api.service import SQS, SNS

app = FastAPI()


@app.post("/sqs/send", tags=["SQS"])
def send_message(request: SendMessageRequest):
    service = SQS()
    return service.send(request.message)


@app.get("/sqs/receive", tags=["SQS"])
def receive_message():
    service = SQS()
    return service.receive()


@app.post("/sqs/delete", tags=["SQS"])
def delete_message(request: DeleteMessageRequest):
    service = SQS()
    return service.delete(request.receipt_handle)


@app.post("/sns/publish", tags=["SNS"])
def publish_message(request: SendMessageRequest):
    service = SNS()
    return service.publish(request.message)
