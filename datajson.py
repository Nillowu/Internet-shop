#-*- coding:utf-8 -*-
import json
from data import data

class datajson(data):
    def read(self):
        with open(self.getInp(),"r", encoding="utf-8") as read_file:
            data=json.load(read_file)
        for k in data.keys():
            if k=='Products':
                    for a in data[k]:
                        code,nameofproduct,price,unitMeasure=0,"",0,""
                        for ak in a.keys():
                            if ak=="Code":code=a[ak]
                            if ak=="Nameofproduct":nameofproduct=a[ak]
                            if ak=="Price":price=a[ak]
                            if ak=="UnitMeasure":unitMeasure=a[ak]
                        self.getShop().createProduct(code,nameofproduct,price,unitMeasure)
            if k=='Clients':
                for a in data[k]:
                    code,surname,name,secname,address,phone,regularity=0,"","","","","",False
                    for ak in a.keys():
                        if ak=="Code":code=a[ak]
                        if ak=="Surname":surname=a[ak]
                        if ak=="Name":name=a[ak]
                        if ak=="Secname":secname=a[ak]
                        if ak=="Address":address=a[ak]
                        if ak=="Phone":phone=a[ak]
                        if ak=="Regularity":regularity=a[ak]
                    self.getShop().createClient(code,surname,name,secname,address,phone,regularity)
            if k=='Sales':
                for a in data[k]:
                    code,client,dateofsale,dateofdelivery,quantity,product=0,None,"","",0,[]
                    for ak in a.keys():
                        if ak=="Code":code=a[ak]
                        if ak=="Client":client=self.getShop().getClient(int(a[ak]))
                        if ak=="DateOfSale":dateofsale=a[ak]
                        if ak=="DateOfDelivery":dateofdelivery=a[ak]
                        if ak=="Quantity":quantity=a[ak]
                        if ak=="Products":product=a[ak]
                    self.getShop().createSale(code,client,dateofsale,dateofdelivery,quantity)
                    sale=self.getShop().getSale(code)
                    if product:
                        for a in product:
                            sale.appendProduct(self.getShop().getProduct(a))
    def write(self):
        data={'Products':[],'Clients':[],'Sales':[]}
        for c in self.getShop().getProductList():
            pr={}
            pr['Code']=c.getCode()
            pr['Nameofproduct']=c.getNameofproduct()
            pr['Price']=c.getPrice()
            pr['UnitMeasure']=c.getUnitMeasure()
            data['Products'].append(pr)
        for c in self.getShop().getClientList():
            cl={}
            cl["Code"] = c.getCode()
            cl["Surname"] = c.getSurname()
            cl["Name"] = c.getName()
            cl["Secname"] = c.getSecname()
            cl["Address"] = c.getAddress()
            cl["Phone"] = c.getPhone()
            cl["Regularity"] = c.getRegularity()
            data['Clients'].append(cl)
        for c in self.getShop().getSaleList():
            sl={}

            sl["Code"] = c.getCode()
            if c.getClient():pc=c.getClient().getCode()
            else:pc=""
            sl["Client"] = pc
            sl["DateOfSale"] = c.getDateOfSale()
            sl["DateOfDelivery"] = c.getDateOfDelivery()
            sl["Quantity"] = c.getQuantity()
            sl["Products"] = c.getProductCodes()
            data['Sales'].append(sl)
        with open(self.getOut(), "w", encoding="utf-8") as write_file:
            json.dump(data, write_file, indent=1, ensure_ascii=False)
