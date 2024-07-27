from PyQt5.QtWidgets import QLineEdit
from editForm import editForm



class productsEditForm(editForm):
    def __init__(self,parent=None,shop=None):
        editForm.__init__(self,shop=shop,parent=parent)
        self.__nameofproductEdit=QLineEdit()
        self.__priceEdit=QLineEdit()
        self.__unitMeasureEdit=QLineEdit()
        self.addLabel('Название', 0, 0)
        self.addNewWidget(self.__nameofproductEdit, 0, 1)
        self.addLabel('Цена', 1, 0)
        self.addNewWidget(self.__priceEdit, 1, 1)
        self.addLabel('Единица измерения', 2, 0)
        self.addNewWidget(self.__unitMeasureEdit, 2, 1)
        if self.getShop().getProductList():
            self.setCurrentCode(self.getShop().getProductList()[0].getCode())


    def update(self):
        if self.getCurrentCode() in self.getShop().getProductCodes():
            self.__nameofproductEdit.setText(self.getShop().getProduct(self.getCurrentCode()).getNameofproduct())
            self.__priceEdit.setText(str(self.getShop().getProduct(self.getCurrentCode()).getPrice()))
            self.__unitMeasureEdit.setText(str(self.getShop().getProduct(self.getCurrentCode()).getUnitMeasure()))
          
         
           
            
    def editClick(self):
        self.getShop().getProduct(self.getCurrentCode()).setNameofproduct(self.__nameofproductEdit.text())
        self.getShop().getProduct(self.getCurrentCode()).setPrice(self.__priceEdit.text())
        self.getShop().getProduct(self.getCurrentCode()).setUnitMeasure(self.__unitMeasureEdit.text())
        
    def newClick(self):
        code=self.getShop().getProductNewCode()
        self.getShop().createProduct(code=code)
        self.getShop().getProduct(code).setNameofproduct(self.__nameofproductEdit.text())
        self.getShop().getProduct(code).setPrice(self.__priceEdit.text())
        self.getShop().getProduct(code).setUnitMeasure(self.__unitMeasureEdit.text()) 
        self.setCurrentCode(code)



    def delClick(self):
        self.getShop().removeProduct(self.getCurrentCode())
