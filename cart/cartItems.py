from menu.menuDecorator import menuDecorator
class cartItems:
    def __init__(self,menu:menuDecorator,quantity) -> None:
        self.quantity = quantity
        self.item = menu