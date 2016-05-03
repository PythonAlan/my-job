#!/usr/bin/env python3
#antuor:Alan

import re
import requests

import threading
import time
from time import ctime,sleep

from queue import Queue


keywords_a=[
    'ELPLP80',
    'ELPLP23',
    'ELPLP29',
    'NP14LP',
    'POA-LMP126',
    'ELPLP66',
]



keywords_b=[
    'VIP230W0.8E20.8',
    'VIP240W0.8E20.9N',
    'NP30LP',
    'LMP-C162',
    'VT70LP',
]



keywords_c= [
    'TLPLV4',
    'POA-LMP131',
    'BL-FP240A',
    'VLT-XD3200LP',
    'ET-LAD35',
    'BL-FU240A',
    '20-01032-20',


]

keywords_d =[
    'ELPLP76',
    'VLT-HC3800LP',
    'BL-FP240C',
    '5811116765-S',
    'ELPLP69',
    'BL-FP200H',

]


keywords_e = [
    '5100MP',
    'RLC-057',
    'ELPLP71',
    'ELPLP64',
    'BL-FS300B',
]


Re_rule = '<span class="a-size-base a-color-price s-price a-text-bold">(.*?)</span>'

headers_am = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36'}

def Scraper(kw):
    for i in kw:
        url_keyword = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords={}'.format(i)
        url_Epharos = 'http://www.amazon.com/s/ref=nb_sb_noss?url=srs%3D9143518011%26search-alias%3Dspecialty-aps&field-keywords={}'.format(i)
        response = requests.get(url_keyword,headers=headers_am)
        response_a = requests.get(url_Epharos,headers=headers_am)
        price = re.findall(Re_rule,response.text)
        price_e = re.findall(Re_rule,response_a.text)

        print('--------------------------{0}爬去完毕at{1}j结果:\n\n市场价:{2}\n\nEpharos:{3}'.format(i,time.ctime(),price[0],price_e[0]))
    time.sleep(1)


threads = []

t1 = threading.Thread(target=Scraper,args=(keywords_a,))
threads.append(t1)
t2 = threading.Thread(target=Scraper,args=(keywords_b,))
threads.append(t2)
t3 = threading.Thread(target=Scraper,args=(keywords_c,))
threads.append(t3)
t4 = threading.Thread(target=Scraper,args=(keywords_d,))
threads.append(t4)
t5 = threading.Thread(target=Scraper,args=(keywords_e,))
threads.append(t5)


if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()

    print ("all over %s" %ctime())