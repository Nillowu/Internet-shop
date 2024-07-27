from PyQt5.QtWidgets import QMainWindow,QAction,QFileDialog
from PyQt5.QtGui import QIcon
import sys,os
from datasql import datasql
from datajson import datajson
from shop import shop
from tabWidget import tabWidget


class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle(u'Интернет магазин')
        self.shop=shop()
        self.datajson=datajson(self.shop)
        self.datasql=datasql(self.shop)
        self.tabWidget=tabWidget(self.shop,self)
        self.setCentralWidget(self.tabWidget)
        self.tabWidget.update()

        self.new=QAction(QIcon(),'New',self)
        self.new.setStatusTip('New database')
        self.new.triggered.connect(self.newAction)
        self.openjson=QAction(QIcon(),'Open JSON',self)
        self.openjson.setStatusTip('Open data from JSON')
        self.openjson.triggered.connect(self.openJSONAction)
        self.opensql=QAction(QIcon(),'Open SQL',self)
        self.opensql.setStatusTip('Open data from SQL')
        self.opensql.triggered.connect(self.openSQLAction)
        self.savejson=QAction(QIcon(),'Save JSON',self)
        self.savejson.setStatusTip('Save data to JSON')
        self.savejson.triggered.connect(self.saveJSONAction)
        self.savesql=QAction(QIcon(),'Save SQL',self)
        self.savesql.setStatusTip('Save data to SQL')
        self.savesql.triggered.connect(self.saveSQLAction)
        self.menubar=self.menuBar()
        self.menufile=self.menubar.addMenu('&File')
        self.menufile.addAction(self.new)
        self.menufile.addSeparator()
        self.menufile.addAction(self.openjson)
        self.menufile.addAction(self.opensql)
        self.menufile.addSeparator()
        self.menufile.addAction(self.savejson)
        self.menufile.addAction(self.savesql)
        self.statusBar()
    def newAction(self):
        self.shop.clear()
        self.tabWidget.update()
    def openJSONAction(self):
        filename=QFileDialog.getOpenFileName(self,u'Открыть JSON',os.getcwd(),u"*.json")[0]
        if filename:
            self.shop.clear()
            self.datajson.readFile(filename)
            self.tabWidget.update()
    def openSQLAction(self):
        filename=QFileDialog.getOpenFileName(self,u'Открыть SQL',os.getcwd(),u"*.sqlite")[0]
        if filename:
            self.shop.clear()
            self.datasql.readFile(filename)
            self.tabWidget.update()
    def saveJSONAction(self):
        filename=QFileDialog.getSaveFileName(self,u'Сохранить JSON',os.getcwd(),u"*.json")[0]
        if filename:self.datajson.writeFile(filename)
    def saveSQLAction(self):
        filename=QFileDialog.getSaveFileName(self,u'Сохранить SQL',os.getcwd(),u"*.sqlite")[0]
        if filename:self.datasql.writeFile(filename)