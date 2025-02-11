from pydantic import BaseModel


class FeedbackModel(BaseModel):
    title: str
    message: str


class TransactionModel(BaseModel):
    instrumentId: str
    quantity: int
    price: float
    purchase_date: str
