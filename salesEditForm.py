from PyQt5.QtWidgets import QVBoxLayout,QLineEdit,QDateEdit,QPushButton,QLabel,QSpinBox,QFileDialog
from PyQt5 import QtCore
from editForm import editForm
from dbComboBox import dbComboBox
from clientsCombo import clientsCombo
from productsCombo import productsCombo
from datetime import datetime
from productsListWidget import productsListWidget
from dbListWidget import dblistWidget



class salesEditForm(editForm):
    def __init__(self,parent=None,shop=None):
        editForm.__init__(self,shop=shop,parent=parent)
        self.__productsListWidget=productsListWidget(shop=shop)
        self.__removeButton=QPushButton(u'удалить')
        self.__productsCombo=productsCombo(shop=shop)
        self.__appendButton=QPushButton(u'добавить')
        self.__clientsCombo=clientsCombo(shop=shop)
        self.__dateOfSaleEdit=QDateEdit()
        self.__dateOfDeliveryEdit=QDateEdit()
        self.__quantityEdit=QLineEdit()

   
        self.addLabel('Товары', 1, 0)
        self.addNewWidget(self.__productsListWidget,1,1)
        self.addNewWidget(self.__removeButton,1,2)
        self.addNewWidget(self.__productsCombo,2,1)
        self.addNewWidget(self.__appendButton,2,2)
        self.addLabel('Клиент', 3, 0)
        self.addNewWidget(self.__clientsCombo, 3, 1)
        self.addLabel('Дата продажи', 4, 0)
        self.__dateOfSaleEdit.setDisplayFormat('dd.MM.yy')
        self.__dateOfSaleEdit.setCalendarPopup(True)
        self.addNewWidget(self.__dateOfSaleEdit, 4, 1)
        self.addLabel('Дата доставки', 5, 0)
        self.__dateOfDeliveryEdit.setDisplayFormat('dd.MM.yy')
        self.__dateOfDeliveryEdit.setCalendarPopup(True)
        self.addNewWidget(self.__dateOfDeliveryEdit, 5, 1)
        self.addLabel('Количество', 6, 0)
        self.addNewWidget(self.__quantityEdit, 6, 1)
        self.__removeButton.clicked.connect(self.removeProduct)
        self.__appendButton.clicked.connect(self.appendProduct)


        if self.getShop().getSaleList():
            self.setCurrentCode(self.getShop().getSaleList()[0].getCode())
        

    def update(self):
        if self.getCurrentCode() in self.getShop().getSaleCodes():
            self.__productsListWidget.setCurrentRec(self.getCurrentCode())
            self.__productsCombo.setCurrentRec(self.getCurrentCode())
            self.__clientsCombo.setCurrentRec(self.getCurrentCode())
            date_str = self.getShop().getSale(self.getCurrentCode()).getDateOfSale()
            date_obj = datetime.strptime(date_str, '%d.%m.%y')
            self.__dateOfSaleEdit.setDate(date_obj)
            date_str = self.getShop().getSale(self.getCurrentCode()).getDateOfDelivery()
            date_obj = datetime.strptime(date_str, '%d.%m.%y')
            self.__dateOfDeliveryEdit.setDate(date_obj)
            self.__quantityEdit.setText(str(self.getShop().getSale(self.getCurrentCode()).getQuantity()))

    def removeProduct(self):
        code=self.__productsListWidget.getCurrentCode()
        if code:
            self.__productsListWidget.removeSelected()
            self.__productsCombo.addItem(code,self.getShop().getProduct(code).getNameofproduct())

    def appendProduct(self):
        code=self.__productsCombo.getCurrentCode()
        if code:
            self.__productsCombo.removeItem(self.__productsCombo.currentIndex())
            self.__productsListWidget.addItem(code,self.getShop().getProduct(code).getNameofproduct())


    def editClick(self):
      
        self.getShop().getSale(self.getCurrentCode()).clearProductList()
        for c in self.__productsListWidget.getCodes():
            self.getShop().getSale(self.getCurrentCode()).appendProduct(self.getShop().getProduct(c))
        self.getShop().getSale(self.getCurrentCode()).setClient(self.getShop().getClient(self.__clientsCombo.getCurrentCode()))
        self.getShop().getSale(self.getCurrentCode()).setDateOfSale(self.__dateOfSaleEdit.text())
        self.getShop().getSale(self.getCurrentCode()).setDateOfDelivery(self.__dateOfDeliveryEdit.text())
        self.getShop().getSale(self.getCurrentCode()).setQuantity(self.__quantityEdit.text())


    def newClick(self):
        code=self.getShop().getSaleNewCode()
        self.getShop().createSale(code=code)
        for c in self.__productsListWidget.getCodes():
            self.getShop().getSale(code).appendProduct(self.getShop().getProduct(c))
        self.getShop().getSale(code).setClient(self.getShop().getClient(self.__clientsCombo.getCurrentCode()))
        self.getShop().getSale(code).setDateOfSale(self.__dateOfSaleEdit.text())
        self.getShop().getSale(code).setDateOfDelivery(self.__dateOfDeliveryEdit.text())
        self.getShop().getSale(code).setQuantity(self.__quantityEdit.text())
       
        self.setCurrentCode(code)


    def delClick(self):
        self.getShop().removeSale(self.getCurrentCode())



