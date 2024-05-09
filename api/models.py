from pydantic import BaseModel


class SendMessageRequest(BaseModel):
    message: str


class DeleteMessageRequest(BaseModel):
    receipt_handle: str
