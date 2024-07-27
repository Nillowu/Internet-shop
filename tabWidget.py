from PyQt5.QtWidgets import QTabWidget
import sys,os
from clientsPage import clientsPage
from productsPage import productsPage
from salesPage import salesPage

class tabWidget(QTabWidget):
    def __init__(self,shop,parent=None):
        QTabWidget.__init__(self,parent)
        self.__clientsPage=clientsPage(shop=shop)
        self.addTab(self.__clientsPage,u"Клиенты")
        self.__productsPage=productsPage(shop=shop)
        self.addTab(self.__productsPage,u"Товары")
        self.__salesPage=salesPage(shop=shop)
        self.addTab(self.__salesPage,u"Продажа")
        self.currentChanged.connect(self.update)
    def update(self):
        self.__clientsPage.update()
        self.__productsPage.update()
        self.__salesPage.update()