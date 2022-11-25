from application.model import User, Admin, UserAccount
from flask import render_template
class SystemInterface:
    def __init__(self):
        pass
    def showMainPage(self):
        return render_template('index.html')
    def showGoods(self, id_item: int):
        return render_template('shop.html')
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
        return render_template('register.html')

    def __checkForCorrectData(self, data: list)->bool:
        return True

    def writeUserData(self, userData:list):
        file = open("application\\data.txt","a")
        file.write(userData[0]+userData[1])
        file.close()

    def goToEntrance(self):
        pass

class Enrtance:
    def checkPassword(self, pwd:list)->bool:
        file = open("application\\data.txt","r")
        res = False
        if pwd in "".join(file.readlines()):
            res = True
            print(1)
        file.close()
        return res

    def checkLogin(self, login: list)->bool:
        file = open("application\\data.txt","r")
        res = False
        if login in "".join(file.readlines()):
            res = True
            print(1)
        file.close()
        return res
    def signIn():
        pass
