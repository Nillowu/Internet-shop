from PyQt5.QtWidgets import QListWidget
from rowCode import rowCode
from shopWidget import shopWidget

class dblistWidget(QListWidget,shopWidget):
    def __init__(self,parent=None,shop=None):
        QListWidget.__init__(self,parent)
        shopWidget.__init__(self,shop)
        self.__rowCode=rowCode()
    def clear(self):
        self.__rowCode.clear()
        QListWidget.clear(self)
    def addItem(self,code,text):
        self.__rowCode.appendRowCode(self.count(),code)
        QListWidget.addItem(self,text)
    def removeSelected(self):
        self.__rowCode.removeRow(self.currentRow())
        for item in self.selectedItems():
            self.takeItem(self.row(item))
    def getCurrentCode(self):return self.__rowCode.getCode(self.currentRow())
    def setCurrentRec(self,value):
        self.__currentRec=value
        self.update()
    def getCurrentRec(self):return self.__currentRec
    def getCodes(self):return self.__rowCode.getCodes()
    def update(self):pass