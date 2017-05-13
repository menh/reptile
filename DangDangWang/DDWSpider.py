# -*- coding:utf-8 -*-

import re
import csv
import requests
import sys
reload (sys)
class DDWspider(object):
    def __init__(self):
        print 'start...'
    #get source pagecode
    def getSource(self,url):
        html=requests.get(url)
        return html.text
    #change URL
    def changePage(self,url,totalPage):
        page_group=[]
        for i in range(totalPage):
            newPage=re.sub(r'/pg(.*?)-cp', '/pg'+'%s'%(i+1)+'-cp', url, re.S)
            page_group.append(newPage)
        return page_group
    #get every book info
    def getEveryBook(self,source):
        everyOne = re.findall('(class="inner".*?</li>)', source, re.S)[1:]
        return everyOne
    #get book info
    def getInfo(self,eachBook):
        info={}
        # include title, author, public, price, discount  
        info['title']=re.search('<a title="(.*?)"', eachBook, re.S).group(1)  
        info['author']=re.search('''''name='P_zz' title='(.*?)'>''', eachBook, re.S)  
        if info['author'] == None:  #调试过程中发现有一本书的结构不一样  
            info['author']=re.search('span>(.*?)</p', eachBook, re.S).group(1)  
        else:  
            info['author']= info['author'].group(1)  
        info['public']=re.search('''''name='P_cbs' title='(.*?)'>''', eachBook, re.S).group(1)  
        info['price']=re.search('''''yen;(.*?)<''', eachBook, re.S).group(1)  
        info['discount']=re.search('''''price_s">(.*?)<''', eachBook, re.S).group(1)  
        return info  
    #save Info use CSV
    def saveInfo(self, bookInfo):  
        with open('infoBook.csv', 'wb') as csvfile:  
            f=csv.writer(csvfile, delimiter=' ')  
            f.writerow(['title', 'author', 'public', 'price', 'discount'])  
            for each in bookInfo:  
                f.writerow([(each['title'], each['author'], each['public'], each['price'], each['discount'])])
if __name__ == '__main__':  
    bookInfo=[]  
    url = 'http://category.dangdang.com/pg1-cp01.36.11.00.00.00-shlist.html'  
    dangdangSpider=DDWspider()  
    allLinks = dangdangSpider.changePage(url, 5)  
    for link in allLinks:  
        print u'processing...' + link  
        html = dangdangSpider.getSource(link)  
        everyBook = dangdangSpider.getEveryBook(html)  
        for each in everyBook:  
            info = dangdangSpider.getInfo(each)  
            bookInfo.append(info)  
        print bookInfo  
    dangdangSpider.saveInfo(bookInfo)  