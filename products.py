#Products (Name, Price, UnitMeasure)
from general import general
class products(general):
    def __init__(self, code=0, nameofproduct='', price=0, unitMeasure=''):
        general.__init__(self, code)
        self.setNameofproduct(nameofproduct)
        self.setPrice(price)
        self.setUnitMeasure(unitMeasure)

    def setNameofproduct(self, nameofproduct):
        self.__nameofproduct = nameofproduct
    def setPrice(self, price):
        self.__price = price
    def setUnitMeasure(self, unitMeasure):
        self.__unitMeasure = unitMeasure

    def getNameofproduct(self):
        return self.__nameofproduct
    def getPrice(self):
        return self.__price
    def getUnitMeasure(self):
        return self.__unitMeasure

    def printProducts(self):
        return str(self.getNameofproduct() + ', ' + str(self.getPrice()) + ', ' + self.getUnitMeasure())