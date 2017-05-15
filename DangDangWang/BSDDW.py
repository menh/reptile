# -*- coding:utf-8 -*-

import re
import csv
import requests
import sys
import urllib2
import urllib
import zlib
import sys
from bs4 import BeautifulSoup
type = sys.getfilesystemencoding()
class DDWspider(object):
    def __init__(self):
        print 'start...'
    def getSource(self,url):
        request=urllib2.Request(url)
        response=urllib2.urlopen(request)
        soup=BeautifulSoup(response)
        print soup.select('ul[class="bigimg"]').encoding(type)
        return soup
if __name__ == '__main__':  
    bookInfo=[]  
    url = 'http://category.dangdang.com/pg1-cp01.36.11.00.00.00-shlist.html'
    dangdangSpider=DDWspider();
    html=dangdangSpider.getSource(url)