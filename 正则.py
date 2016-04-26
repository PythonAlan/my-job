#!/usr/bin/env python3
#antuor:Alan


import re
template = "Hello [first_name] [last_name], \
 Thank you for purchasing [product_name] from [store_name]. \
 The total cost of your purchase was [product_price] plus [ship_price] for shipping. \
 You can expect your product to arrive in [ship_days_min] to [ship_days_max] business days. \
 Sincerely, \
 [store_manager_name]"
# assume dic has all the replacement data
# such as dic['first_name'] dic['product_price'] etc...
dic = {
 "first_name" : "John",
 "last_name" : "Doe",
 "product_name" : "iphone",
 "store_name" : "Walkers",
 "product_price": "$500",
 "ship_price": "$10",
 "ship_days_min": "1",
 "ship_days_max": "5",
 "store_manager_name": "DoeJohn"
}
def multiple_replace(dic, text):
    pattern = "|".join(map(lambda key : re.escape("["+key+"]"), dic.keys()))
    return re.sub(pattern, lambda m: dic[m.group()[1:-1]], text)
print (multiple_replace(dic, template))
##############################################
"""匹配IP地址"""
s = '123.168.156.143'
m = re.match('([0-9]{1,3}\.){3}\d{1,3}',s)
print(m.group())