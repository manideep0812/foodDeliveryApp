from abc import ABC, abstractmethod
class paymentTemplate(ABC):
    def processPayment(self,amount:int)->None:
        self.validate(amount)
        self.authenticate()
        self.deduct(amount)
        self.notifyUser()
    
    @abstractmethod
    def validate(self,amount:int)->None:
        pass
    @abstractmethod
    def authenticate(self)->None:
        pass
    @abstractmethod
    def deduct(self,amount:int):
        pass
    def notifyUser(self):
        print("payment success")