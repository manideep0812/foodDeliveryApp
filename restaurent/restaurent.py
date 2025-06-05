import generateID
from menu import Menu


from typing import List

class restaurant:
    def __init__(self,restaurentName,address,isAvailable):
        self.restaurentName = restaurentName
        self.address = address
        self.isAvailable = isAvailable
        self.restaurentId = generateID()
        self.menu = List[Menu] = []
        