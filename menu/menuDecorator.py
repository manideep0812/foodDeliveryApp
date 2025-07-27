from abc import ABC, abstractmethod
from menu.menu import Menu

class menuDecorator(ABC):
    def __init__(self,menu:Menu) -> None:
        self.menu = menu
    @abstractmethod
    def getPrice(self) -> int:
        pass
        
    @abstractmethod
    def getDecription(self) -> str:
        pass


class baseMenu(menuDecorator):
    def __init__(self, menu: Menu) -> None:
        super().__init__(menu)
    def getPrice(self) -> int:
        return self.menu.getPrice()
    def getDecription(self) -> str:
        return self.menu.getDescription()
    
class cheeseDecorator(menuDecorator):
    def __init__(self, menu: Menu) -> None:
        super().__init__(menu)
    def getPrice(self) -> int:
        return self.menu.getPrice() + 10
    def getDecription(self) -> str:
        return self.menu.getDescription() + " extra cheese added"
    

        