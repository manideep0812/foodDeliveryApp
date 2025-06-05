import generateID

class Menu:
        def __init__(self,name,price,rating,isAvailable,description,category,restaurentId,deliveryTime):
            self.name= name
            self.price= price
            self.rating= rating
            self.isAvailable= isAvailable
            self.description= description
            self.category= category
            self.restaurantId= restaurentId
            self.deliveryTime= deliveryTime
            self.itemId= generateID()
        
        def toggleAvailable(self):
            self.isAvailable = not self.isAvailable

        def updatePrice(self,updatedprice):
            self.price = updatedprice

        def getPrice(self):
            return self.price
        
        def getDescription(self):
            return self.description