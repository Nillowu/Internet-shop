#-*- coding:utf-8 -*-
class data:
    def __init__(self, shop=None,inp='',out=''):
        self.setShop(shop)
        self.setInp(inp)
        self.setOut(out)
    def setShop(self,value): self.__shop=value
    def setInp(self,value): self.__inp=value
    def setOut(self,value): self.__out=value
    def getShop(self): return self.__shop
    def getInp(self): return self.__inp
    def getOut(self): return self.__out

    def readFile(self,filename):
        self.setInp(filename)
        self.read()
    def writeFile(self,filename):
        self.setOut(filename)
        self.write()
    def read(self): pass
    def write(self): pass

