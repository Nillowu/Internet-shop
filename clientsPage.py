from page import page
from clientsTable import clientsTable
from clientsEditForm import clientsEditForm

class clientsPage(page):
    def __init__(self,shop,parent=None):
        page.__init__(self,shop=shop,parent=parent)
        self.setTable(clientsTable(shop=shop,parent=parent))
        self.setForm(clientsEditForm(shop=shop,parent=parent))
        self.setConnect()