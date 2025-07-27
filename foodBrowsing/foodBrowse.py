from foodBrowsing.sortStrategy import ISortStrategy
from menu.menu import Menu
class foodBrowse:
    def __init__(self,sortstrategy:ISortStrategy) -> None:
        self.sortStrategy= sortstrategy
        pass
    def browse(self,menuList:list[Menu]) -> list[Menu]:
        return self.sortStrategy.sort(menuList)