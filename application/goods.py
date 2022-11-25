class Item:
    __count = 0
    def __init__(self, itemType:int, price:float, image:str, name:str, weight:float):
        self.__itemType=itemType
        self.__price=price
        self.__image=image
        self.__name=name
        self.__weight=weight
        self.__id=Item.__count
        Item.__count+=1

    @property
    def price(self):
        return self.__price

    @property
    def image(self):
        return self.__image

    @property
    def name(self):
        return self.__name

    @property
    def weight(self):
        return self.__weight

    @property
    def itemType(self):
        return self.__itemType

    @property
    def id(self):
        return self.__id


class ItemComments:
    def __init__(self, id, comment, rating):
        self.__id = id
        self.__comment = comment
        self.__rating = rating


class Search:
    def __init__(self, id, text):
        self.__id = id
        self.__text = text
    def search(self, text:str):
        pass
    def searchResult()->str:
        pass


class BasketFavorites:
    def __init__(self, id: int, itemData: list, searchResults: str):
        self.__id=id
        self.__itemData = itemData
        self.__searchResults = searchResults

    def proceedToCheckoutOrder():
        pass
    def addItemToFavourites():
        pass
    def deleteFromFavourites():
        pass


class Ordering: 
    def __init__(self, orderDate, orderTime):
        self.__orderDate = orderDate
        self.__orderTime = orderTime
    
    def choiceOfPaymentMethod():
        pass

    def chooseDeliveryMethod():
        pass

    def leaveComment():
        pass

    def leaveRating():
        pass

    def chooseGoodsCount():
        pass

    def calculateOrderCost():
        pass


class PaymentMethod:
    def __init__(self):
        pass