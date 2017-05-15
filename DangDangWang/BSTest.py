# -*- coding: utf-8 -*-
# @Author: HaonanWu
# @Date:   2016-12-22 20:37:38
# @Last Modified by:   HaonanWu
# @Last Modified time: 2016-12-22 21:27:30
import urllib2
import urllib
import re  

from bs4 import BeautifulSoup  


url = "https://www.packtpub.com/all"
url = 'http://category.dangdang.com/pg1-cp01.36.11.00.00.00-shlist.html'
try:
    request=urllib2.Request(url)
    html=urllib2.urlopen(request)
    #html = urllib2.urlopen(url)  
except urllib2.HTTPError as e:
    print e
    exit()

soup_packtpage = BeautifulSoup(html)  
print soup_packtpage.prettify().encode('gb18030')
print soup_packtpage.title.encode('gb18030')
file =open("title.txt","w")
file.write(str(soup_packtpage.title))
all_book_title = soup_packtpage.find_all("div", class_="book-block-title")  

price_regexp = re.compile(u"\s+\$\s\d+\.\d+")  

for book_title in all_book_title:  
    try:
        print "Book's name is " + book_title.string.strip()
    except AttributeError as e:
        print e
        exit()
    book_price = book_title.find_next(text=price_regexp)  
    try:
        print "Book's price is "+ book_price.strip()
    except AttributeError as e:
        print e
        exit()
    print ""