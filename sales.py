#Sales (Product, Client, DateOfSale, DateOfDelivery, Quantity)
from general import general
from productsList import ProductsList

class Sales(general):
    def __init__(self, code=0,client=None, dateOfSale='', dateOfDelivery='', quantity=0):
        general.__init__(self, code)
        self.__ProductsList = ProductsList()
        self.setClient(client)
        self.setDateOfSale(dateOfSale)
        self.setDateOfDelivery(dateOfDelivery)
        self.setQuantity(quantity)



    def calculateTotalCost(self):
        if self.__ProductsList and self.__client:
            summ = 0 
            for product in self.__ProductsList.getItems():
                summ += int(product.getPrice())
            if summ > 5000:

                self.__client.setRegularity(True)
        total_cost = 0
        k=1
        for product in self.__ProductsList.getItems():
                total_cost += int(product.getPrice())
        if self.__ProductsList and self.__client:
            f=self.__client.getRegularity()
            
            if f==True:
                k=k-0.02
        if total_cost>=7000:
            k=k-0.05
        total_cost=int(total_cost*k)
        return total_cost


   
    def setClient(self, client):
        self.__client = client
    def setDateOfSale(self, dateOfSale):
        self.__dateOfSale = dateOfSale
    def setDateOfDelivery(self, dateOfDelivery):
        self.__dateOfDelivery = dateOfDelivery
    def setQuantity(self, quantity):
        self.__quantity = quantity


    def getClient(self):
        return self.__client
    def getClientFIO(self):
        return self.__client.getFIO()
    def getClientAddress(self):
        return self.__client.getAddress()
    def getClientPhone(self):
        return self.__client.getPhone()
    def getClientRegularity(self):
        return self.__client.getRegularity()
    def getClientCode(self):
        if self.getClient():return self.getClient().getCode()
        else: return 0
    def getPublName(self):
        if self.getClient():return self.getClient().getSurname()
        else: return ''
    def getDateOfSale(self):
        return self.__dateOfSale
    def getDateOfDelivery(self):
        return self.__dateOfDelivery
    def getQuantity(self):
        return self.__quantity



    def appendProduct(self,value):self.__ProductsList.appendItem(value)
    def removeProduct(self,value):self.__ProductsList.removeItem(value)
    def clearProductList(self):self.__ProductsList.clear()
    def getProduct(self,code):return self.__ProductsList.findByCode(code)
    def getProductList(self):return self.__ProductsList.getItems()
    def getProductCodes(self):return self.__ProductsList.getCodes()
    def getProductBiblioStr(self):return self.__ProductsList.getBiblioStr()









    def printSales(self):
        if self.getProduct(): prod = self.getProduct().printProducts()
        else: prod = '-'
        if self.getClient(): clnt = self.getClient().printClients()
        else: clnt = '-'
        return str('Продукт: ' + prod + '\nКлиент: ' + clnt + '\nДата продажи = ' + self.getDateOfSale() + '\nДата доставки = ' + self.getDateOfDelivery() + '\nКоличество: ' + str(self.getQuantity()))