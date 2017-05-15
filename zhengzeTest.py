# -*- coding:utf-8 -*-
import re
def pythonSubDemo():
    inputStr="hello 123 world 456";
    def _add111(matched):
        intStr=matched.group("number")
        intValue=int(intStr)
        addValue=intValue+111
        addValueStr=str(addValue)
        return addValueStr
    replacedStr=re.sub("(?P<number>\d+)",_add111,inputStr)
    print replacedStr
if __name__=="__main__":
    pythonSubDemo()