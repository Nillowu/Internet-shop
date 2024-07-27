#Clients (Surname, Name, Secname, Address, Phone, Regularity)
from general import general
class clients(general):
    def __init__(self, code=0, surname='', name='', secname='', address='', phone='', regularity=False):
        general.__init__(self, code)
        self.setSurname(surname)
        self.setName(name)
        self.setSecname(secname)
        self.setAddress(address)
        self.setPhone(phone)
        self.setRegularity(regularity)

    def setSurname(self, surname):
        self.__surname = surname
    def setName(self, name):
        self.__name = name
    def setSecname(self, secname):
        self.__secname = secname
    def setAddress(self, address):
        self.__address = address
    def setPhone(self, phone):
        self.__phone = phone
    def setRegularity(self, regularity):
        self.__regularity = regularity

    def getSurname(self):
        return self.__surname
    def getName(self):
        return self.__name
    def getSecname(self):
        return self.__secname
    def getAddress(self):
        return self.__address
    def getPhone(self):
        return self.__phone
    def getRegularity(self):
        return self.__regularity

    def getFIO(self):
        return str(self.getSurname() + ' ' + self.getName()[0] + '. ' + self.getSecname()[0] + '.')

    def printClients(self):
        return str(self.getFIO() + ', ' + self.getAddress() + ', ' + self.getPhone())