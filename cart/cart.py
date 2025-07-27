from cart.cartItems import cartItems
from menu.menuDecorator import menuDecorator


class cart:
    totalAmount= 0
    cartitems = []

    def addToCart(self,menu:menuDecorator,quantity):
        self.cartitems.append(cartItems(menu,quantity))
        self.calculateTotal()
    
    def removeFromCart(self,menu:menuDecorator,quantity):
        for item in self.cartitems:
            if item.item == menu:
                if item.quantity > quantity:
                    item.quantity -= quantity
                else:
                    self.cartitems.remove(item)
                    break
        self.calculateTotal()
    
    def calculateTotal(self):
        sum = 0
        for i in self.cartitems:
            sum += (i.item.getPrice() * i.quantity)
        self.totalAmount = sum
    




        
