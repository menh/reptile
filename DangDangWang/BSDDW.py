# -*- coding:utf-8 -*-

import re
import csv
import requests
import sys
import urllib2
import urllib
import zlib
import sys
import re
from bs4 import BeautifulSoup
type = sys.getfilesystemencoding()
class DDWspider(object):
    def __init__(self):
        print 'start...'
    def getSource(self,url):
        request=urllib2.Request(url)
        response=urllib2.urlopen(request)
        soup=BeautifulSoup(response)

        EveryLine=[]
        info={}
        line=1
        file=open('title2.txt','w+')
        while soup.find_all('li',class_='line'+str(line)):
            s=soup.find_all('li',class_='line'+str(line))
            ss=s[0].encode('gb18030')
            EveryLine.append(ss)
            info['title']=re.search('.*?title="(.*?)".*?',ss,re.S).group(1)
            info['price']=re.search('.*?<span class="search_now_price">(.*?)</span>.*?',ss,re.S).group(1)
            print info['price']
            print info['title']
            file.write(info['title'])
            file.write(info['price'])
            file.write('\n')
            line=line+1
        return soup
if __name__ == '__main__':
    bookInfo=[]
    url = 'http://category.dangdang.com/pg1-cp01.36.11.00.00.00-shlist.html'
    dangdangSpider=DDWspider();
    html=dangdangSpider.getSource(url)
