








import  requests
from lesson4.base import BaseObj
from lesson4.part3.func import print_json
from  lesson4.part3.auth import auth_token

from lesson4.part3.RequestUtil import RequestUtil














class CreatCouponApi(RequestUtil):
	""" """
	def __init__(self, **kwargs):
		super().__init__()
		self.host = "http://144.34.200.237:8080/"
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
				super(CreatCouponApi.Body.SmsCouponProductCategoryRelation, self).__init__(**kwargs)

		class SmsCouponproductRelation(BaseObj):
			""" None"""
			def __init__(self,**kwargs):
				self.couponId = None
				self.id = None
				self.productId = None
				self.productName = None
				self.productSn = None
				super(CreatCouponApi.Body.SmsCouponproductRelation, self).__init__(**kwargs)

	class Resp(object):
		def __init__(self):
			super(CreatCouponApi.Resp, self).__init__()
			self.code = None
			self.data = None
			self.message = None


	def set_token(self):
		self.update_headers(dict(Authorization=auth_token))
		return self

	def update_headers(self, param):
		pass


api_obj = CreatCouponApi().set_token().send_request()
print(api_obj.resp.__dict__)




















