import requests
from requests.auth import HTTPProxyAuth
#
# curl -kvx forcepoint.corp.internal.citizensbank.com:80 "https://internaljobs.citizensbank.com/"
#
proxy_string = 'http://forcepoint.corp.internal.citizensbank.com:80'

s = requests.Session()
s.proxies = {"http": proxy_string , "https": proxy_string}
# s.auth = HTTPProxyAuth(user,password)

#r = s.get('http://www.google.com') # OK
#print(r.status_code)

r = s.get('https://internaljobs.citizensbank.com/') # OK
# print(r.text)
print(r.status_code)
               
