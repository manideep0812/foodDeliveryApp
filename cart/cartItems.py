from menu.menu import Menu
class cartItems:
    def __init__(self,menu:Menu,quantity) -> None:
        self.quantity = quantity
        self.item = menu