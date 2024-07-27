from dbComboBox import dbComboBox

class productsCombo(dbComboBox):

    def update(self):
        self.clear()
        for a in self.getShop().getProductList():
            if not(a in self.getShop().getSale(self.getCurrentRec()).getProductList()):
                self.addItem(a.getCode(),a.getNameofproduct())
