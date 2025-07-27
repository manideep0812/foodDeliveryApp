from abc import ABC

from payment.templateSubclasses import creditCardPayment, upiPayment
class paymentStrategy(ABC):
    def pay(self,amount:int):
        pass

class creditCardStrategy(paymentStrategy):
    def __init__(self) -> None:
        self._creditCard = creditCardPayment()
    def pay(self, amount: int):
        self._creditCard.processPayment(amount)

class upiStrategy(paymentStrategy):
    def __init__(self) -> None:
        self._upi = upiPayment()
    def pay(self, amount: int):
        self._upi.processPayment(amount)


