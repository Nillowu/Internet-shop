#Online shop
import os
from shop import Shop
from datajson import datajson
from datasql import datasql

shop = Shop()

json = datajson(shop,"data.json","new.json")
sql = datasql(shop,"data.sqlite","new.sqlite")

json.read()
sql.write()