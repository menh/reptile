__author__ ='MH'
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
class QSBK:
    #init function
    def __init__(self):
        self.pageIndex=1 #pageIndex
        self.user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers={'User-Agent':self.user_agent} # set headerss
        self.stories=[] #for store stories
        self.enable=False
    # get utf-8 page
    def getPage(self,pageIndex):
        try:
            url='http://www.qiushibaike.com/hot/page/'+str(pageIndex) # set url
            request=urllib2.Request(url,headers=self.headers)
            response=urllib2.urlopen(request)
            pageCode=response.read().decode('utf-8')#turn the page to utf-8
            return pageCode	
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print 'get ERROR the reason is :',e.reason
                return None
    def getPageItems(self,pageIndex):
        pageCode=self.getPage(pageIndex)
        if not pageCode:
            print "page download error"
            return None
        pattern=re.compile('<div class="content">.*?<span>(.*?)</span>.*?</div>',re.S)
        items=re.findall(pattern,pageCode)
        pageStories=[]
        for item in items:
            pageStories.append(item)
        return pageStories
    #download page
    def loadPage(self):
        if self.enable==True:
            if len(self.stories)<2:
                pageStories=self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex+=1
    #get one stories
    def getOneStory(self,pageStories,page):
        for story in pageStories:
            input=raw_input()
            self.loadPage()
            if input=='Q':
                self.enable=False
                return
            print story
    def start(self):
        print u'start to read QSBK,ENTER to next,Q to exit'
        self.enable=True
        self.loadPage()
        nowPage=0
        while self.enable:
            if len(self.stories)>0:
                pageStories=self.stories[0]
                nowPage+=1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)
spider=QSBK()
spider.start()