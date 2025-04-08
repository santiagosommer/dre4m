from enum import Enum


class PaymentMethod(str, Enum):
    credit_card = "Credit Card"
    debit_card = "Debit Card"
