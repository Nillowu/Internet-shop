from dbComboBox import dbComboBox


class clientsCombo(dbComboBox):
    def update(self):
        self.clear()
        for p in self.getShop().getClientList():
            self.addItem(p.getCode(),str(p.getSurname()))
        if self.getShop().getSale(self.getCurrentRec()).getClient():
            self.setCurrentCode(self.getShop().getSale(self.getCurrentRec()).getClient().getCode())

