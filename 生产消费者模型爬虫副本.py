#!/usr/bin/env python3
#antuor:Alan

import re
import requests

import threading
import time
from time import ctime,sleep

from queue import Queue




keywords= [
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
#requests库的参数之一，浏览器伪装

class Producer(threading.Thread):
    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name=t_name)
        self.data=queue
    def run(self):
        for i in keywords:
            url_keyword = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords={}'.format(i)
            #遍历所有关键词链接

            self.data.put(url_keyword)     #放入生产者队列
            time.sleep(1)
class Consumer_even(threading.Thread):
    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name=t_name)
        self.data=queue
    def run(self):
        for i  in range(20):
            val_even = self.data.get()   #消费者，在队列取
            print(val_even)
            response = requests.get(val_even,headers=headers_am)
            self.data.task_done()
            # requests.get(post)(url,params) ，参数以字典形式传入
            price = re.findall('<span class="a-size-base a-color-price s-price a-text-bold">(.*?)</span>',response.text)
            #(.*?)非贪婪模式
            print(price)

def main():
    queue = Queue()
    producer = Producer('Pro',queue)
    consumer = Consumer_even('Con_even',queue)

    producer.start()
    #consumer.setDaemon(True)
    consumer.start()

    producer.join()
    consumer.join()
    print("结束!!!!!!!!!!!!")
if __name__ =="__main__":
    main()
