#-*- coding:utf-8 -*-
from general import general
class generalList(general):
    def __init__(self):self.__list=[]

    def clear(self):self.__list=[]

    def findByCode(self,code):
        for l in self.__list:
            if l.getCode()==code:return l

    def getCodes(self):return [s.getCode() for s in self.__list]

    def getNewCode(self):
        codes = self.getCodes()
        if not codes:
            return 1
        else:return max(codes) + 1

    def getItems(self):return [s for s in self.__list]

    def appendItem(self, value):
        if isinstance(value,general):self.__list.append(value)

    def removeItem(self,value):
        if isinstance(value,general):self.__list.remove(value)
        if isinstance(value,int):self.__list.remove(self.findByCode(value))