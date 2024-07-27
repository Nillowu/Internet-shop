from PyQt5.QtWidgets import QTableWidgetItem
from dbTableWidget import dbTableWidget



class productsTable(dbTableWidget):
    def __init__(self,shop,parent=None):
        dbTableWidget.__init__(self,shop=shop,parent=parent,header=[u'Название',u'Цена',u'Единица измерения'])
    def setData(self):
        self.setRowCount(len(self.getShop().getProductCodes()))
        r=0
        for a in self.getShop().getProductList():
            self.setItem(r,0,QTableWidgetItem(a.getNameofproduct()))
            self.setItem(r,1,QTableWidgetItem(str(a.getPrice())))
            self.setItem(r,2,QTableWidgetItem(a.getUnitMeasure()))
            self.appendRowCode(r,a.getCode())
            r+=1

