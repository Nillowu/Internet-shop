from PyQt5.QtWidgets import QTableWidgetItem
from dbTableWidget import dbTableWidget



class clientsTable(dbTableWidget):
    def __init__(self,shop,parent=None):
        dbTableWidget.__init__(self,shop=shop,parent=parent,header=[u'Фамилия',u'Имя',u'Отчество',u'Адрес',u'Телефон',u'Постоянный клиент'])
    def setData(self):
        self.setRowCount(len(self.getShop().getClientCodes()))
        r=0
        for a in self.getShop().getClientList():
            self.setItem(r,0,QTableWidgetItem(a.getSurname()))
            self.setItem(r,1,QTableWidgetItem(a.getName()))
            self.setItem(r,2,QTableWidgetItem(a.getSecname()))
            self.setItem(r,3,QTableWidgetItem(a.getAddress()))
            self.setItem(r,4,QTableWidgetItem(a.getPhone()))
            if a.getRegularity()==True:
                self.setItem(r,5,QTableWidgetItem('Постоянный'))
            if a.getRegularity()==False:
                self.setItem(r,5,QTableWidgetItem('Непостоянный'))
            self.appendRowCode(r,a.getCode())
            r+=1



