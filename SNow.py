import requests
from requests.auth import HTTPProxyAuth
#
# curl -kvx forcepoint.corp.internal.citizensbank.com:80 "https://citizensfguat.service-now.com/"
#
curl "https://citizensfguat.service-now.com/api/now/table/problem?sysparm_limit=1" \
--request GET \
--header "Accept:application/json" \
--user 'username':'password'
#
proxy_string = 'http://forcepoint.corp.internal.citizensbank.com:80'
#
s = requests.Session()
s.proxies = {"http": proxy_string , "https": proxy_string}
# s.auth = HTTPProxyAuth(user,password)
# s.auth=('david.s.willsey@citizensbank.com', 'xxxxxx')

#r = s.get('http://www.google.com') # OK
#print(r.status_code)

# r = s.get('https://citizensfguat.service-now.com/') # OK
r = s.get('https://citizensfguat.service-now.com/') # OK
# print(r.text)
print(r.status_code)
               
