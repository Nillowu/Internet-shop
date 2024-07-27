from PyQt5.QtWidgets import QTableWidgetItem
from dbTableWidget import dbTableWidget


class salesTable(dbTableWidget):
    def __init__(self,shop,parent=None):
        dbTableWidget.__init__(self,shop=shop,parent=parent,header=[u'Товары',u'Клиент',u'Дата продажи',u'Дата доставки',u'Количество',u'Итоговая стоимость'])
    def setData(self):
        self.setRowCount(len(self.getShop().getSaleCodes()))
        r=0
        for a in self.getShop().getSaleList():
            self.setItem(r,0,QTableWidgetItem(a.getProductBiblioStr()))
            if a.getClient():self.setItem(r,1,QTableWidgetItem(str(a.getClient().getSurname())))
            else:self.setItem(r,1,QTableWidgetItem(''))
            self.setItem(r,2,QTableWidgetItem(str(a.getDateOfSale())))
            self.setItem(r,3,QTableWidgetItem(str(a.getDateOfDelivery())))
            self.setItem(r,4,QTableWidgetItem(str(a.getQuantity())))
            self.setItem(r,5,QTableWidgetItem(str(a.calculateTotalCost())))
            self.appendRowCode(r,a.getCode())
            r+=1
 