from payment.paymentTemplate import paymentTemplate

class creditCardPayment(paymentTemplate):
    def validate(self, amount: int) -> None:
        print("validating credir card for payment of",amount)
    def authenticate(self) -> None:
        print("Authenticating through otp")
    def deduct(self, amount: int):
        print(amount,"deducted from credit card")


class upiPayment(paymentTemplate):
    def validate(self, amount: int) -> None:
        print("validating upi for payment of",amount)
    def authenticate(self) -> None:
        print("Authenticating through otp")
    def deduct(self, amount: int):
        print(amount,"deducted via upi")

