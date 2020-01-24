set http_proxy=forcepoint.corp.internal.citizensbank.com:80
set https_proxy=https_proxy=https://j040967:xxxxxx@forcepoint.internal.citizensbank.com:443

pip install cx_Oracle

(base) D:\Anaconda3>pip --proxy "admin\j040967:xxxxxxxx@forcepoint.corp.internal.citizensbank.com:80"  --trusted-host files.pythonhosted.org --trusted-host pypi.org install cx_Oracle
Collecting cx_Oracle
  Downloading https://files.pythonhosted.org/packages/49/5a/c445cf6702b7ce9c46ea
85406195bc29ece54ed82dc5534f115db47d5069/cx_Oracle-7.3.0-cp37-cp37m-win_amd64.wh
l (189kB)
    100% |████████████████████████████████| 194kB 2.8MB/s
Installing collected packages: cx-Oracle
Successfully installed cx-Oracle-7.3.0

(base) D:\Anaconda3>
#
# curl -kvx forcepoint.corp.internal.citizensbank.com:80 "https://citizensbank-prod.saas.appdynamics.com:443/controller/rest/applications/"
#

import cx_Oracle


connstr = 'tdw/go2beach_12@lxribshare01-scan:1527/svc_ssd11ppr_tdw'
conn = cx_Oracle.connect(connstr)
con = cx_Oracle.connect('username/password@localhost')

cursor = cx_Oracle.cursor()

    cursor.execute("create table student(srollno number, \ 
                    name varchar2(10), efees number(10, 2)")
# Program to create a table in Oracle database 
import cx_Oracle 
  
try: 
  
    con = cx_Oracle.connect('scott/tiger@localhost') 
      
    # Now execute the sqlquery 
    cursor = con.cursor() 
    cursor.execute("insert into student values(19585, Niranjan Shukla, 72000") 
      
    # commit that insert the provided data 
    con.commit() 
      
    print("value inserted successful") 
  
except cx_Oracle.DatabaseError as e: 
    print("There is a problem with Oracle", e) 
  
# by writing finally if any error occurs 
# then also we can close the all database operation 
finally: 
    if cursor: 
        cursor.close() 
    if con:
       con.close() 

