from generalList import generalList
from products import products

class ProductsList(generalList):
	def appendItem(self, value):
		if isinstance(value, products): generalList.appendItem(self, value)

	def createItem(self, code, nameofproduct='', price=0, unitMeasure=''):
		if code in self.getCodes():
			print(f'Продукт с кодом {code} уже существует')
		else:
			p=products(code, nameofproduct, price, unitMeasure)
			generalList.appendItem(self,p)
			return p
	def newItem(self, nameofproduct='', price=0, unitMeasure=''):
		p=products(self.getNewCode(), nameofproduct, price, unitMeasure)
		generalList.appendItem(self,p)
		return p

	def getBiblioStr(self):
		s=''
		for i in self.getItems():
			s+=i.getNameofproduct()+', '
		if s:s=s[:-2]
		return s



	def printProductsList(self):
		s = ''
		for i in self.getItems():
			s+=i.printProducts() + '\n'
		return s