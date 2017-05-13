import MySQLdb
def mysql_test():  
    try:  
        sql='select * from stu'  
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='test1',port=3306)  
        cur=conn.cursor()  
        cur.execute(sql)  
        print 'conn:%s' %conn  
        print 'cur: %s' %cur  
        cur.close()  
        conn.close()  
    except MySQLdb.Error,e:  
        print 'MySQL Error %d:%s' %(e.args[0],e.args[1])  
  
if __name__=="__main__":  
    mysql_test()  