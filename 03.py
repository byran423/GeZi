# -- coding: utf-8 --

# import requests
# url = "http://httpbin.org/get"
# data = {"key":"value","abc":"xyz"}
# response = requests.get(url, data)
# print(response.text)

def hello_somebody(name):
    print("url= " + name)
    url = name
    response = requests.post(url)
    print(response.json())


if __name__ == "__main__":
    import requests
    import sys

    # url = 'http://httpbin.org/post'
    # data = {'key':'value', 'abc':'xyz'}
    # response = requests.post(url,data)
    # print(response.json())

    name = sys.argv[1]
    hello_somebody(name)






