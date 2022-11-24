

class userAccount:
    __counter = 0
    def __init__(self, *args, **kwargs):
        self.__userData = list(args)
        self.__id = super.__counter
        super.__counter+=1

    @property
    def userData(self):
        return self.__userData[:]

    @property
    def id(self):
        return self.__id