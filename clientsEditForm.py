from PyQt5.QtWidgets import QLineEdit
from editForm import editForm



class clientsEditForm(editForm):
    def __init__(self,parent=None,shop=None):
        editForm.__init__(self,shop=shop,parent=parent)
        self.__surnameEdit=QLineEdit()
        self.__nameEdit=QLineEdit()
        self.__secnameEdit=QLineEdit()
        self.__addressEdit=QLineEdit()
        self.__phoneEdit=QLineEdit()
        self.__regularityEdit=QLineEdit()
        self.addLabel('Фамилия', 0, 0)
        self.addNewWidget(self.__surnameEdit, 0, 1)
        self.addLabel('Имя', 1, 0)
        self.addNewWidget(self.__nameEdit, 1, 1)
        self.addLabel('Отчество', 2, 0)
        self.addNewWidget(self.__secnameEdit, 2, 1)
        self.addLabel('Адрес', 3, 0)
        self.addNewWidget(self.__addressEdit, 3, 1)
        self.addLabel('Телефон', 4, 0)
        self.addNewWidget(self.__phoneEdit, 4, 1)
        if self.getShop().getClientList():
            self.setCurrentCode(self.getShop().getClientList()[0].getCode())


    def update(self):
        if self.getCurrentCode() in self.getShop().getClientCodes():
            self.__surnameEdit.setText(self.getShop().getClient(self.getCurrentCode()).getSurname())
            self.__nameEdit.setText(self.getShop().getClient(self.getCurrentCode()).getName())
            self.__secnameEdit.setText(self.getShop().getClient(self.getCurrentCode()).getSecname())
            self.__addressEdit.setText(self.getShop().getClient(self.getCurrentCode()).getAddress())
            self.__phoneEdit.setText(self.getShop().getClient(self.getCurrentCode()).getPhone())
            
    def editClick(self):
        self.getShop().getClient(self.getCurrentCode()).setSurname(self.__surnameEdit.text())
        self.getShop().getClient(self.getCurrentCode()).setName(self.__nameEdit.text())
        self.getShop().getClient(self.getCurrentCode()).setSecname(self.__secnameEdit.text())
        self.getShop().getClient(self.getCurrentCode()).setAddress(self.__addressEdit.text())
        self.getShop().getClient(self.getCurrentCode()).setPhone(self.__phoneEdit.text())
        

    def newClick(self):
        code=self.getShop().getClientNewCode()
        self.getShop().createClient(code=code)
        self.getShop().getClient(code).setSurname(self.__surnameEdit.text())
        self.getShop().getClient(code).setName(self.__nameEdit.text())
        self.getShop().getClient(code).setSecname(self.__secnameEdit.text())
        self.getShop().getClient(code).setAddress(self.__addressEdit.text())
        self.getShop().getClient(code).setPhone(self.__phoneEdit.text())
       
        self.setCurrentCode(code)



    def delClick(self):
        self.getShop().removeClient(self.getCurrentCode())


