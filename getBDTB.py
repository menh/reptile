__author__='MH'
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
class BDTB:
    def __init__(self,baseUrl,seeLZ):
        self.baseUrl=baseUrl
        self.seeLZ=seeLZ
    #get the page code
    def getPage(self,pageNum):
        try:
            url=self.baseUrl+str(self.seeLZ)+'&pn='+str(pageNum)
            url='http://tieba.baidu.com/f?kw=%E6%97%85%E8%A1%8C'
            #print url
            request=urllib2.Request(url)
            response=urllib2.urlopen(request)
            print response.read()
            return response
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u'connect failed',e.reason
                return None
baseURL='http://tieba.baidu.com/p/3138733512'
bdtb=BDTB(baseURL,1)
bdtb.getPage(1)
			