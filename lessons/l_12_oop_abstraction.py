from abc import ABC, abstractmethod


def l_12_oop_abstraction():
    class Payment(ABC):
        @abstractmethod
        def process_payment(self, amount: float):
            raise NotImplementedError(
                "This method should be overridden in subclasses")

    class CreditCardPayment(Payment):
        def __init__(self, card_number: str, amount: float) -> None:
            self.card_number = card_number
            self.amount = amount

        def process_payment(self, amount: float):
            print(
                f"Processing credit card payment of {amount}  \
                using card {self.card_number}")

    class PayPalPayment(Payment):
        def __init__(self, email: str, amount: float) -> None:
            self.email = email
            self.amount = amount

        def process_payment(self, amount: float):
            print(
                f"Processing PayPal payment of {amount} using email {self.email}")

    credit_card_payment = CreditCardPayment(
        card_number="1234-5678-9012-3456", amount=100.0)

    print(credit_card_payment.process_payment(amount=100.0))
    paypal_payment = PayPalPayment(email="test@mail.com", amount=50.0)
    print(paypal_payment.process_payment(amount=50.0))
