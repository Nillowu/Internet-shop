from generalList import generalList
from sales import Sales

class SalesList(generalList):
	def appendItem(self, value):
		if isinstance(value, Sales): generalList.appendItem(self, value)

	def createItem(self, code, client=None, dateOfSale='', dateOfDelivery='', quantity=0):
		if code in self.getCodes():
			print(f'Продажа с кодом {code} уже существует')
		else:
			p=Sales(code, client, dateOfSale, dateOfDelivery, quantity)
			generalList.appendItem(self,p)
			return p
	def newItem(self,client=None, dateOfSale='', dateOfDelivery='', quantity=0):
		p=Sales(self.getNewCode(), client, dateOfSale, dateOfDelivery, quantity)
		generalList.appendItem(self,p)
		return p

	def printSalesList(self):
		s = ''
		for i in self.getItems():
			s+=i.printSales() + '\n'
		return s