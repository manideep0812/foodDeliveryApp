from abc import ABC, abstractmethod
from menu.menu import Menu

class ISortStrategy(ABC):
    @abstractmethod
    def sort(self,menuList: list[Menu]) -> list[Menu]:
        pass

class sortByPrice(ISortStrategy):
    def sort(self,menuList:list[Menu]):
        return sorted(menuList, key=lambda item: item.price)


class sortByRating(ISortStrategy):
    def sort(self,menuList:list[Menu]):
        return sorted(menuList, key=lambda item: item.rating)


class sortByDeliveryTime(ISortStrategy):
    def sort(self,menuList:list[Menu]):
        return sorted(menuList, key=lambda item: item.deliveryTime)
