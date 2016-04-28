#!/usr/bin/env python3
#antuor:Alan
import requests
import re

url = 'http://www.crowdfunder.com/browse/deals'


data = {
    'entities_only':'true',
    'page':'1'

}

html = requests.post(url,data=data)
title = re.findall('"card-title">(.*?)</div>',html.text)
for each in title:
    print(each)