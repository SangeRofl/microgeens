class Account:
    def __init__(self, *args, **kwargs):
        self.__userData = []
    def handleRecievedData():
        pass


class AdminAccount(Account):
    __counter = 0
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__id = AdminAccount.__counter
        AdminAccount.__counter+=1

    @property
    def userData(self):
        return self.__adminData[:]

    @property
    def id(self):
        return self.__id

    def __giveAdminRights(adminData: list)->bool:
        pass

    def __changeGoods():
        pass

    def __changeMenuNames():
        pass

    def interactionWithInterface():
        pass


class UserAccount(Account):
    __counter = 0
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__id = UserAccount.__counter
        UserAccount.__counter+=1

    @property
    def userData(self):
        return self.__userData[:]

    @property
    def id(self):
        return self.__id

    def __giveUserRights(userData: list)->bool: 
        pass

    def interactionWithInterface():
        pass

    def checkoutOrder():
        pass

    def addToBasket():
        pass

    def contactTechnicalSupport(idAdmin: int):
        pass


class User:
    def __init__(self, fio: str, login: str, password: str, email: str, phoneNumber:int):
        self.fio = fio
        self.login = login
        self.__password = password
        self.__email = email
        self.__phoneNumber = phoneNumber
    
    @property
    def password(self):
        return self.__password

    @property
    def email(self):
        return self.__email

    @property
    def phoneNumber(self):
        return self.__phoneNumber


class Admin(User):
    def __init__(self, fio: str, login: str, password: str, email: str, phoneNumber:int):
        super().__init__(self, fio, login, password, email, phoneNumber)
        self.__specLogin=login


class Message:
    def __init__(self, id, text, time, data):
        self.__id = id
        self.__text = text
        self.__time = text
        self.__data = data
    
    @property
    def id(self):
        return self.__id

    @property
    def text(self):
        return self.__text
    
    @property
    def text(self):
        return self.__text
    
    @property
    def data(self):
        return self.__data


class SupportChat:
    def __init__(self):
        self.__messages = []
    def getMessage(self, message):
        self.__messages.append(message)
    @property
    def messages(self):
        return self.__messages  