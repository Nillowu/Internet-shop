from page import page
from productsTable import productsTable
from productsEditForm import productsEditForm

class productsPage(page):
    def __init__(self,shop,parent=None):
        page.__init__(self,shop=shop,parent=parent)
        self.setTable(productsTable(shop=shop,parent=parent))
        self.setForm(productsEditForm(shop=shop,parent=parent))
        self.setConnect()
