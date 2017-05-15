# -*-coding:utf-8 -*-
import urllib
import urllib2
import sys
type = sys.getfilesystemencoding()
url = 'http://category.dangdang.com/pg1-cp01.36.11.00.00.00-shlist.html'
request=urllib2.Request(url)
response=urllib2.urlopen(request)
print response.read().decode("gbk").encode(type)


