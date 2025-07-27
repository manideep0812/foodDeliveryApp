from customer.customer import customer
from restaurent.restaurentAdmin import restaurentAdmin
from restaurent.restaurent import restaurant
from menu.menu import Menu


restro1 = restaurant("amro","hyd",True)
pizza = Menu("italian pizza",100,4.5,True,"carrot","veg",restro1.restaurentId,30)
butterChicken = Menu("butter Chicken",200,4.0,True,"rajasthan style","non-veg",restro1.restaurentId,40)

admin1 = restaurentAdmin("raju",restro1)
admin1.addMenuItem(pizza)
admin1.addMenuItem(butterChicken)

#customer
manideep = customer("manideep","manideep@gmail.com",12345678,"hyd")
print(restro1.getAllAvailableItems())

manideep.cart.addToCart(pizza,1)
print(manideep.cart.totalAmount)
manideep.cart.addToCart(butterChicken,2)
print(manideep.cart.totalAmount)
manideep.cart.removeFromCart(pizza,1)
print(manideep.cart.totalAmount)
manideep.cart.removeFromCart(butterChicken,1)
print(manideep.cart.totalAmount)