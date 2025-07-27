from customer.customer import customer
from enums import orderStatus
from foodBrowsing.sortStrategy import sortByPrice, sortByRating
from menu.menuDecorator import baseMenu, cheeseDecorator
from payment.paymentProcessor import paymentProcessor
from payment.strategy import upiStrategy
from payment.templateSubclasses import upiPayment
from restaurent.restaurentAdmin import restaurentAdmin
from restaurent.restaurent import restaurant
from foodBrowsing.foodBrowse import foodBrowse
from menu.menu import Menu


restro1 = restaurant("amro","hyd",True)
pizza = Menu("italian pizza",100,4.5,True,"carrot","veg",restro1.restaurentId,30)
butterChicken = Menu("butter Chicken",200,4.0,True,"rajasthan style","non-veg",restro1.restaurentId,40)

admin1 = restaurentAdmin("raju",restro1)
admin1.addMenuItem(pizza)
admin1.addMenuItem(butterChicken)

#customer
manideep = customer("manideep","manideep@gmail.com",12345678,"hyd")

print('available items in restaurent',restro1.getAllAvailableItems())

print('items available in restaurent sorted by price:')
food = foodBrowse(sortByPrice())
for i in food.browse(restro1.menuList):
    print(i.name)

# preparing items
cheesepizza = cheeseDecorator(pizza)
pizza = baseMenu(pizza)
baseButterChicken = baseMenu(butterChicken)

#adding items into cart
manideep.cart.addToCart(pizza,1)#100
manideep.cart.addToCart(cheesepizza,1)#110
manideep.cart.addToCart(baseButterChicken,1)#200

#total cart amount
print("total bill:",manideep.cart.totalAmount)

#place the order
manideep_order = manideep.placeOrder()
print("order status ->",manideep_order.orderStatus)

#order prepared
manideep_order.updateOrderStatus(orderStatus.PREPARED)
print("order status ->",manideep_order.orderStatus)

#out-for-delivery
manideep_order.updateOrderStatus(orderStatus.OUTFORDELIVERY)
print("order status ->",manideep_order.orderStatus)

payment = paymentProcessor(upiStrategy(),manideep_order.totalAmount,manideep_order.orderId,manideep.userId)

payment.process()