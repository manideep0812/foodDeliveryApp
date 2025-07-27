from generateID import generateID
from menu.menu import Menu

class restaurant:
    def __init__(self,restaurentName:str,address:str,isAvailable:bool):
        self.restaurentName = restaurentName
        self.address = address
        self.isAvailable = isAvailable
        self.restaurentId = generateID()
        self.menuList : list[Menu] = []

    def toggleAvailable(self):
        self.isAvailable = not self.isAvailable

    def getAllAvailableItems(self):
        items = []
        for i in self.menuList:
            if i.isAvailable:
                items.append(i.name)
        return items
    
    def getItemsByCategory(self,category:str):
        items = []
        for i in self.menuList:
            if i.isAvailable and i.getCategory == category :
                items.append(i.name)
        return items
