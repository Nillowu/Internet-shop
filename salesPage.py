from page import page
from salesTable import salesTable
from salesEditForm import salesEditForm

class salesPage(page):
    def __init__(self,shop,parent=None):
        page.__init__(self,shop=shop,parent=parent)
        self.setTable(salesTable(shop=shop,parent=parent))
        self.setForm(salesEditForm(shop=shop,parent=parent))
        self.setConnect()