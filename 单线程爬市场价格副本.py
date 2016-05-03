#!/usr/bin/env python3
#antuor:Alan

import re
import requests

import threading
import time
from time import ctime








keywords_c= [
    'TLPLV4',
    'POA-LMP131',
    'BL-FP240A',
    'VLT-XD3200LP',
    'ET-LAD35',
    'BL-FU240A',
    '20-01032-20',
    'ELPLP76',
    'VLT-HC3800LP',
    'BL-FP240C',
    '5811116765-S',
    'ELPLP69',
    'BL-FP200H',
    'NPLM35',
    '5100MP',
    'NPLM38',
    'RLC-057',
    'ELPLP71',
    'ELPLP64',
    'BL-FS300B',


]







headers_am = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36'}

def Scraper(kw):
    for i in kw:
        url_keyword = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords={}'.format(i)
        response = requests.get(url_keyword,headers=headers_am)
        price = re.findall('<span class="a-size-base a-color-price s-price a-text-bold">(.*?)</span>',response.text)

        print('--------------------------{0}爬去完毕at{1}j结果{2}----------------------------'.format(i,time.ctime(),price))

    print ("all over %s" %ctime())

if __name__ == "__main__":
    Scraper(keywords_c)