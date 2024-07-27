#-*- coding:utf-8 -*-
from productsList import ProductsList
from clientsList import clientsList
from salesList import SalesList

class shop:
    def __init__(self):
        self.__ProductsList = ProductsList()
        self.__clientsList = clientsList()
        self.__SalesList = SalesList()

    def clear(self):
        self.__ProductsList.clear()
        self.__clientsList.clear()
        self.__SalesList.clear()




    def createProduct(self, code=0, name='', price=0, unitMeasure=''):
        self.__ProductsList.createItem(code,name,price,unitMeasure)
    def newProduct(self, name='', price=0, unitMeasure=''):
        self.__ProductsList.newItem(name,price,unitMeasure)
    def removeProduct(self, value):
        self.__ProductsList.removeItem(value)
        for b in self.__SalesList.getItems():
            product = b.getProduct(value)
            if product is not None:
                b.removeProduct(product)
    def getProduct(self, code):
        return self.__ProductsList.findByCode(code)
    def getProductList(self):
        return self.__ProductsList.getItems()
    def getProductCodes(self):
        return self.__ProductsList.getCodes()
    def getProductNewCode(self):
        return self.__ProductsList.getNewCode()



    def createClient(self, code, surname='', name='', secname='', address='', phone='', regularity=''):
        self.__clientsList.createItem(code, surname, name, secname, address, phone, regularity)
    def newClient(self, surname='', name='', secname='', address='', phone='', regularity=''):
        self.__clientsList.newItem(surname, name, secname, address, phone, regularity)
    def removeClient(self, code):
        self.__clientsList.removeItem(code)
        for b in self.__SalesList.getItems():
            if b.getClient().getCode()==code:
                b.setClient(None)
    def getClient(self, code):
        return self.__clientsList.findByCode(code)
    def getClientList(self):
        return self.__clientsList.getItems()
    def getClientCodes(self):
        return self.__clientsList.getCodes()
    def getClientNewCode(self):
        return self.__clientsList.getNewCode()



    def createSale(self, code, client=None, dateOfSale='', dateOfDelivery='', quantity=0):
        self.__SalesList.createItem(code, client, dateOfSale, dateOfDelivery, quantity)
    def newSale(self,  client=None, dateOfSale='', dateOfDelivery='', quantity=0):
        self.__SalesList.newItem(client, dateOfSale, dateOfDelivery, quantity)
    def removeSale(self, code):
        self.__SalesList.removeItem(code)
    def getSale(self, code):
        return self.__SalesList.findByCode(code)
    def getSaleList(self):
        return self.__SalesList.getItems()
    def getSaleCodes(self):
        return self.__SalesList.getCodes()
    def getSaleNewCode(self):
        return self.__SalesList.getNewCode()

    def printSale(self):
        return self.__SalesList.printSalesList()