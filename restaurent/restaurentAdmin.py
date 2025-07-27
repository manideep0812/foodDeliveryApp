from menu.menu import Menu
from generateID import generateID

class restaurentAdmin:
    def __init__(self, name: str, restaurent) -> None:
        self.name = name
        self.restaurent = restaurent
        self.restaurentAdminId = generateID()
    
    def addMenuItem(self,menu:Menu):
        self.restaurent.menuList.append(menu)

    def removeMenuItem(self,menu:Menu):
        self.restaurent.menuList.remove(menu)
