






import json,requests
from lesson4.base import BaseObj



def to_dict(obj):
	try:
		return obj.__dict__
	except Exception as e:
		return obj


def obj_to_json(obj):
	""" """
	return json.dumps(obj, default=to_dict)


def to_obj(j):
	try:
		return BaseObj(**j)
	except Exception as e:
		return j


def json_to_obj(j):
	""" """
	return json.loads(json.dumps(j), object_hook=to_obj)


headers = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           "User-Agent": "tester-pc"
           }


class OrderManageCreate(object):
	""" """
	def __init__(self, **kwargs):
		super().__init__()
		self.host = "http://144.34.200.237:8080/"
		self.headers = headers
		self.info = "添加优惠券"
		self.url = "/coupon/create"
		self.method = "post"
		self.body = self.Body(**kwargs)
		self.resp = self.Resp()


	class Body(BaseObj):
		def __init__(self,**kwargs):
			self.amount = 299
			self.enableTime = "2019-11-30T16:00:00.000Z"
			self.minPoint = 10
			self.name = "测试优惠券"
			self.note = "备注内容"
			self.perLimit = 1
			self.platform = 0.1
			self.productCategoryRelationList = []
			self.productRelationList = []
			self.publishCount = 1000
			self.startTime = "2019-11-15T16:00:00,000Z"
			self.type = 0
			self.useType = 0
			self.code = None

		class SmsCouponProductCategoryRelation(BaseObj):
			""" None"""
			def __init__(self,**kwargs):
				self.couponId = None
				self.id: None
				self.parentCategoryName = None
				self.productCategoryId = None
				self.productCategoryName = None
				super(OrderManageCreate.Body.SmsCouponProductCategoryRelation, self).__init__(**kwargs)

		class SmsCouponproductRelation(BaseObj):
			""" None"""
			def __init__(self,**kwargs):
				self.couponId = None
				self.id = None
				self.productId = None
				self.productName = None
				self.productSn = None
				super(OrderManageCreate.Body.SmsCouponproductRelation, self).__init__(**kwargs)

	class Resp(object):
		def __init__(self):
			super(OrderManageCreate.Resp, self).__init__()
			self.code = None
			self.data = None
			self.message = None


	def send_request(self):
		"""
		None
		:return:
		"""
		self.url = self.compose_url()
		json_body = obj_to_json(self.body) if self.body else None
		resp_act = self.__send_request(data=json_body)
		self.resp = json_to_obj(resp_act)
		return self

	def compose_url(self, json_param=None):
		"""拼接完成host+url+param"""
		url = self.host.rstrip('/') + "/" + self.url.lstrip('/')
		return url




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

		def print_json(j):
			print(json.dumps(j,
							 indent=4,
							 ensure_ascii=False))

		if r.status_code == 200:
			response = r.json()
			print_json(response)
			return response
		else:
			print("接口返回为None,HttpCode={}".format(str(r.status_code)) )
			return None


api_obj = OrderManageCreate().send_request()

print(api_obj.resp.__dict__)



















