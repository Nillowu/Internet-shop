from generalList import generalList
from clients import clients

class clientsList(generalList):
	def appendItem(self, value):
		if isinstance(value, clients): generalList.appendItem(self, value)

	def createItem(self, code, surname='', name='', secname='', address='', phone='', regularity=False):
		if code in self.getCodes():
			print(f'Клиент с кодом {code} уже существует')
		else:
			p=clients(code,surname, name, secname, address, phone, regularity)
			generalList.appendItem(self,p)
			return p
	
	def newItem(self, surname='', name='', secname='', address='', phone='', regularity=False):
		p=clients(self.getNewCode(),surname, name, secname, address, phone, regularity)
		generalList.appendItem(self,p)
		return p
	def printClientsList(self):
		s = ''
		for i in self.getItems():
			s+=i.printClients() + '\n'
		return s