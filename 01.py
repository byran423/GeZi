# -- coding: utf-8 --
from urllib import parse
from urllib import request
import socket
import  urllib

# url = 'http://www.baidu.com'
# response = request.urlopen(url,timeout=10)
# print(response.read().decode('utf-8'))
#hee

data = bytes(parse.urlencode({"word":"hello"}),encoding='utf8')
response = request.urlopen("http://httpbin.org/post",data=data)
print(response.read().decode('utf-8'))
#
response2 = request.urlopen("http://httpbin.org/get",timeout=1)
print(response2.read())

try:
    response3=request.urlopen("http://httpbin.org/get",timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT")
