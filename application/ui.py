from application.model import User, Admin, UserAccount
from flask import render_template
class SystemInterface:
    def __init__(self):
        pass
    def showMainPage(self):
        return render_template('index.html')
    def showGoods(id_item: int):
        pass
    def showSystemMenu(self):
        pass
    def showComments(self, comments: list):
        pass
    def showRatings(self, ratings: list):
        pass
    def showUserAccount(self):
        pass
    def showSearhLine(self):
        pass

class EntranceScreen:
    def __init__(self, link:str):
        self.__link= link
    @property
    def link(self):
        return self.__link
    
    def showEntranceScreen(self):
        return render_template('auth.html')

    def linkToTheRegistration(self, link: str)->str:
        pass



class Registration:
    def showRegistrationScreen(self, link):
        pass
    def __checkEntranceData(self, data: list)->bool:
        return True
    def __writeUserData(self, userData:list):
        pass
    def goToEntrance(self):
        pass

class Enrtance:
    def checkPassword(self, pwd:list)->bool:
        return True
    def checkLogin(self, login: list)->bool:
        return True
    def signIn():
        pass
