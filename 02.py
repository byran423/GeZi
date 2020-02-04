# -- coding: utf-8 --

from urllib import request,parse

url = "http://httpbin.org/post"
headers={
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
"Dnt": "1",
"Host": "httpbin.org",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

dict = {
    "name":"value"
}

date = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url=url,data=date,headers=headers,method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))




