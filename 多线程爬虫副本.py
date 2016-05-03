#!/usr/bin/env python3
#antuor:Alan

import re
import requests

import threading
import time
from time import ctime,sleep

url_EB = 'http://www.amazon.com/gp/search/other/ref=sr_sa_p_4?me=A22XNR713HGDVG&rh=n%3A9063592011%2Ck%3Aprojector&bbn=9063592011&keywords=projector&pickerToList=brandtextbin&ie=UTF8&qid=1461902521'
headers_EB = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36'}


url_AML = '''https://www.amazon.com/gp/search/other/ref=sr_sa_p_4?me=A3UJI9WWE6PRP5&rh=i%3Amerchant-items
&pickerToList=brandtextbin&ie=UTF8&qid=1461899728'''
headers_AML ={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36'}


url_DL= 'https://www.amazon.com/gp/search/other/ref=sr_sa_p_4?me=AS7ZU4MN0FPOY&rh=i%3Amerchant-items&pickerToList=brandtextbin&ie=UTF8&qid=1461901862'
headers_DL = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36'}






name = {'a':'ExclusiveBulbs',
        'b':'Amazing Lamps',
        'c':'Dynamic Lamps'}

# listing_count = re.findall('<span class="narrowValue">(.*?)</span',data.text)
# f = dict(map(lambda x,y:[x,y],store_name,listing_count))
#
# for k,v in f.items():
#     print(k,v)







def foo_one(url,headers,name):
    print('--------------------------开始爬去{0}at{1}---------------------------'.format(name,time.ctime()))

    response = requests.get(url,headers=headers)
    store_name = re.findall('<span class="refinementLink">(.*?)</span><span class="narrowValue">(.*?)</span',response.text)
    for i in store_name:
        print(i)
    print('--------------------------爬去完毕{0}at{1}----------------------------'.format(name,time.ctime()))














threads = []
t1 = threading.Thread(target=foo_one,args=(url_EB,headers_EB,name['a']))
threads.append(t1)
t2 = threading.Thread(target=foo_one,args=(url_AML,headers_AML,name['b']))
threads.append(t2)
t3 = threading.Thread(target=foo_one,args=(url_DL,headers_DL,name['c']))
threads.append(t3)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

    print ("all over %s" %ctime())