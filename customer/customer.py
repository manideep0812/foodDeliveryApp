from generateID import generateID
from cart.cart import cart
from order.order import order


class customer:
    def __init__(self,name:str,email:str,phone:int,address:str):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.userId = generateID()
        self.cart = cart()

    def placeOrder(self) -> order:
        cus_order = order(self.cart.totalAmount,self.cart,self.userId,self.address,self.cart.cartitems[0].item.restaurantId)
        return cus_order
