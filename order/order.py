from generateID import generateID
from enums import orderStatus, paymentStatus
from cart.cart import cart

class order:
    def __init__(self,totalAmount,cart:cart,customerID,address,restaurentID) -> None:
        self.totalAmount = totalAmount
        self.orderId = generateID()
        self.orderStatus = orderStatus.PLACED
        self.cart = cart
        self.userID = customerID
        self.paymentStatus = paymentStatus.PENDING
        self.address = address
        self.restaurentID = restaurentID
    
    def updateOrderStatus(self,status):
        self.orderStatus = status

    def cancelOrder(self):
        self.orderStatus = orderStatus.CANCEL

