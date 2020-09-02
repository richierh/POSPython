import xmlrpc


# example

# url = "http://192.168.100.200:8069"
url = "http://192.168.100.200:8069"
db = "TBKamojang"
username = "richie130283@gmail.com"
password = "admin"    
# password = <insert password for your admin user (default: admin)>

import xmlrpc.client
#
# info = xmlrpc.client.ServerProxy('http://192.168.100.200/start').start()
# url, db, username= \
#     info['host'], info['database'], info['user']

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()
print (common.version())
# uid = common.authenticate(db, username, password, {})
uid = common.login(db,username,password)
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
a = models.execute_kw(db, uid, password,'res.partner', 'search',[[['is_company', '=', True]]])
print (a)
b = models.execute_kw(db, uid, password, 'product.product', 'search_read', [[]], {'fields': ['description', 'name','list_price'], 'context' :{'lang': "es_ES"}})
print (b)
c = models.execute_kw(db,uid,password,'product.template', 'search_read',[[]],{'fields':['image_1920']})
print (c)