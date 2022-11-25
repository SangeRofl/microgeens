from application.goods import Item
from application.model import User
from application.model import User, Admin
from application.ui import SystemInterface
class System:
    # def __init__(self, interface: SystemInterface):
    #     self.__interface = interface

    def leaveComment(self, text:str, item:Item, user:User):
        pass

    def leaveRating(self, rating:int, item: Item, user: User):
        pass

    def sendMessageToAdmin(self, text: str, target: Admin, source: User):
        pass

    def sendMessageToUser(self, text: str, target: User, source: Admin):
        pass

    def findGoods1(self, string:str)->str:
        pass
    
    def findGoods2(self, text: str, itemName: str, user: User):
        pass
    
    def readGoodsInfo(self, id: Item):
        pass
    
    def runSystemInterface(self):
        pass