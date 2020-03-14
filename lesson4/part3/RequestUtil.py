
import requests
from lesson4.part3.func import *
# from lesson4.part5.common.RequestUtil import RequestUtil


headers = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           "User-Agent": "tester-pc"
           }

class RequestUtil(object):
	def __init__(self):
		self.headers = headers

	def send_request(self):
		"""
		None
		:return:
		"""
		self.url = self.compose_url()
		json_body = obj_to_json(self.body) if self.body else None
		print_json(self.body.__dict__)
		resp_act = self.__send_request(data=json_body)
		# print(str(resp_act))
		self.resp = json_to_obj(resp_act)
		return self


	def compose_url(self, json_param=None):
		"""拼接完成host+url+param"""
		url = self.host.rstrip('/') + "/" + self.url.lstrip('/')
		print(url)
		return url


	def update_headers(self, add_headers={}):
		self.headers.update(add_headers)


	def __send_request(self, data=None):
		"""发送请求并判断r.request_code ==200
		"""
		r = None
		common_condition = dict(url=self.url, headers=self.headers)
		if self.method == "get":
			r = requests.get(**common_condition)
		if self.method == "post":
			r = requests.post(**common_condition, data=data, allow_redirects=False)
		if self.method == "put":
			r = requests.put(**common_condition, data=data)
		if self.method == "delete":
			r = requests.delete(**common_condition, data=data)
		print(r.status_code)
		if str(r.status_code) == "200":
			response = r.json()
			print_json(response)
			return response
		else:
			print("接口返回为None,HttpCode={}".format(str(r.status_code)))
			return None









