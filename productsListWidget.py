from dbListWidget import dblistWidget

class productsListWidget(dblistWidget):
    def update(self):
        self.clear()
        l=self.getShop().getSale(self.getCurrentRec()).getProductList()
        for a in l:
            self.addItem(a.getCode(),a.getNameofproduct())
        if l:self.setCurrentRow(0)

