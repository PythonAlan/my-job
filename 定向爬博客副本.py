#!/usr/bin/env python3
#antuor:Alan
#-*- coding: utf-8 -*-

import requests
from lxml import etree
import datetime,time
import os









class xxoohelper(object):     #易读
    def __init__(self):
        self.url = 'http://www.cnblogs.com/alan-babyblog/'      #初始化
    def getSource(self):
        html = requests.get(self.url).content       #content比text好用，一个返回的是byte,一个返回的是str
        return html
    def getContent(self,html):                     #先大后小
        selector = etree.HTML(html)
        title  = selector.xpath('//div[1]/div[2]/a/text()')[0].strip()  #从列表提取文本
        content = selector.xpath('//div[1]/div[2]/div[1]/div/div[1]/div[3]/div/text()')[0].strip()
        post_time = selector.xpath('//div[1]/div[2]/div[1]/div/div[1]/div[5]/text()')[0].strip()
        send_text = title+content+post_time  #类型是str
        return send_text
    def tosave(self,text):
        with open('myblog.txt','a') as f:
            f.write(('{0}\n').format(text))   #换行
    def tocheck(self,data):
        if not os.path.exists('myblog.txt'):   #判断是否存在文件
            return True
        else:
            with open ('myblog.txt','r') as f:
                existblog = f.readlines()
                #print(data+'\n')
                if data +'\n' in existblog:  #判断是否已经纪录过内容
                    return False
                else:
                    return True
if __name__ == '__main__':      #程序入口
    helper = xxoohelper()  #实例化
    while True :           #while循环不断监控页面
        source = helper.getSource()
        content = helper.getContent(source)
        if helper.tocheck(content):
            post_time = str(datetime.datetime.now())
            print(post_time,'有新内容\n',content)
            helper.tosave(content)
        else:
            print('扫描中......')
            pass
        time.sleep(30)


