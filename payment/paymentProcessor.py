from enums import paymentStatus
from generateID import generateID
from payment.strategy import paymentStrategy


class paymentProcessor:
    def __init__(self,paymentStrategy,amount:int,orderId:str,userId:str):
        self.strategy = paymentStrategy
        self.amount = amount
        self.orderId = orderId
        self.userId = userId
        self.paymentStatus = paymentStatus.INPROGRESS
        self.paymentId = generateID()

    def setStrategy(self,strategy:paymentStrategy):
        self.strategy = strategy
    
    def process(self):
        self.strategy.pay(self.amount)
        self.paymentStatus = paymentStatus.COMPLETED
