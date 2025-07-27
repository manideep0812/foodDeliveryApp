from cart.cartItems import cartItems
from menu.menu import Menu


class cart:
    totalAmount= 0
    cartitems = []

    def addToCart(self,menu:Menu,quantity):
        self.cartitems.append(cartItems(menu,quantity))
        self.calculateTotal()
    
    def removeFromCart(self,menu:Menu,quantity):
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
    




        
