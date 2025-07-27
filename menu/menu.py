from generateID import generateID

class Menu:
        def __init__(self,name:str,price:int,rating:float,isAvailable:bool,description:str,category:str,restaurentId,deliveryTime:int):
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
        
        def getCategory(self) -> str:
            return self.category

        def getPrice(self) -> int:
            return self.price
        
        def getDescription(self) -> str:
            return self.description