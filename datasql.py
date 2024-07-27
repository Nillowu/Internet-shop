#-*- coding:utf-8 -*-
import os
import sqlite3 as db
from data import data
emptydb = """
PRAGMA foreign_keys = ON;

CREATE TABLE Products (
    Code        INTEGER PRIMARY KEY,
    Nameofproduct        TEXT,
    Price       INTEGER,
    UnitMeasure TEXT
);

CREATE TABLE Clients (
    Code       INTEGER     PRIMARY KEY,
    Surname    TEXT,
    Name       TEXT,
    Secname    TEXT,
    Address    TEXT,
    Phone      TEXT,
    Regularity BOOLEAN
);

CREATE TABLE Sales (
    Code           INTEGER     PRIMARY KEY,
    Client         INTEGER     REFERENCES Clients (Code) ON DELETE CASCADE ON UPDATE CASCADE,
    DateOfSale     TEXT,
    DateOfDelivery TEXT,
    Quantity       INTEGER
);
CREATE TABLE Sales_Products (
    Code           INTEGER     PRIMARY KEY AUTOINCREMENT,
    Sales         INTEGER     REFERENCES Sales(Code) ON DELETE CASCADE ON UPDATE CASCADE,
    Products         INTEGER     REFERENCES Products(Code) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE(Sales,Products));

 """

class datasql(data):
    def read(self):
        conn= db.connect(self.getInp())
        curs= conn.cursor()
        curs.execute('select Code,Nameofproduct,Price,UnitMeasure from Products')
        data=curs.fetchall()
        for r in data:self.getShop().createProduct(r[0],r[1],r[2],r[3])
        curs.execute('select Code,Surname,Name,Secname,Address,Phone,Regularity from Clients')
        data=curs.fetchall()
        for r in data:self.getShop().createClient(r[0],r[1],r[2],r[3],r[4],r[5],r[6])
        curs.execute('select Code,Client,DateOfSale,DateOfDelivery,Quantity from Sales')
        data=curs.fetchall()
        for r in data:
            self.getShop().createSale(r[0],self.getShop().getClient(int(r[1])),r[2],r[3],r[4])
        curs.execute('select Sales,Products from Sales_Products')
        data=curs.fetchall()
        for r in data:self.getShop().getSale(r[0]).appendProduct(self.getShop().getProduct(r[1]))
        conn.close()

    def write(self):
        conn = db.connect(self.getOut())
        curs = conn.cursor()
        curs.executescript(emptydb)
        for a in self.getShop().getProductList():
            curs.execute("insert into Products( Code,Nameofproduct,Price,UnitMeasure) values('%s','%s','%s','%s')"%(
                str(a.getCode()),a.getNameofproduct(),a.getPrice(),a.getUnitMeasure()))
        for p in self.getShop().getClientList():
            curs.execute("insert into Clients( Code,Surname,Name,Secname,Address,Phone,Regularity) values('%s','%s','%s','%s','%s','%s','%s')"%(
                 str(p.getCode()),p.getSurname(),p.getName(),p.getSecname(),p.getAddress(),p.getPhone(),p.getRegularity()))
        for b in self.getShop().getSaleList():
            if b.getClient():pc=str(b.getClient().getCode())
            else:pc=""
            bc=str(b.getCode())
            curs.execute("insert into Sales(Code,Client,DateOfSale,DateOfDelivery,Quantity) values('%s','%s','%s','%s','%s')"%(
                bc,str(pc),b.getDateOfSale(),b.getDateOfDelivery(),str(b.getQuantity())))
            for ac in b.getProductCodes():
                curs.execute("insert into Sales_Products(Sales,Products) values('%s','%s')"%(bc,str(ac)))
        conn.commit()
        conn.close()
