import requests
from requests.auth import HTTPProxyAuth
from pprint import pprint
import json
#
# curl -kvx forcepoint.corp.internal.citizensbank.com:80 "https://www.linkedin.com/"
#
proxy_string = 'http://forcepoint.corp.internal.citizensbank.com:80'

s = requests.Session()
s.proxies = {"http": proxy_string , "https": proxy_string}
# s.auth = HTTPProxyAuth(user,password)
# s.auth=('davewillsey@cox.net', 'Shirley1')

#r = s.get('http://www.google.com') # OK
#print(r.status_code)

# r = s.get('https://www.linkedin.com/company/travelers') # OK
r = s.get('https://www.linkedin.com/', auth=('davewillsey@cox.net', 'Shirley1')) # OK
# print(r.text)
print(r.status_code)
               
