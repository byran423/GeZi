

import requests,json
from lesson4.base import BaseObj
from lesson4.part4.BaseOrderManageService import BaseOrderManageService
# from  lesson4.part3.auth import auth_token
# from lesson4.part3.RequestUtil import RequestUtil



class CreateCouponApi(BaseOrderManageService):
	""" """
	def __init__(self, **kwargs):
		super().__init__()
		# self.host = "http://144.34.200.237:8080/"
		self.info = "添加优惠券"
		self.url = "/coupon/create"
		self.method = "post"
		self.body = self.Body(**kwargs)
		self.resp = self.Resp()


	class Body(BaseObj):
		def __init__(self,**kwargs):
			self.amount = None
			self.enableTime = None
			self.minPoint = None
			self.name = None
			self.note = None
			self.perLimit = None
			self.platform = None
			# self.productCategoryRelationList = []
			self.productCategoryRelationList = [self.SmsCouponProductCategoryRelation()]
			# self.productRelationList = []
			self.productRelationList = [self.SmsCouponProductRelation()]
			self.publishCount = None
			self.startTime = None
			self.type = None
			self.useType = None
			self.code = None
			self.count = None
			self.id = None
			self.memberLevel = None
			self.receiveCount = None
			self.useCount = None
			super(CreateCouponApi.Body, self).__init__(**kwargs)


		class SmsCouponProductCategoryRelation(BaseObj):
			""" None"""
			def __init__(self,**kwargs):
				self.couponId = None
				self.id: None
				self.parentCategoryName = None # 父分类名称
				self.productCategoryId = None# None
				self.productCategoryName = None  # 产品分类名称
				super(CreateCouponApi.Body.SmsCouponProductCategoryRelation, self).__init__(**kwargs)


		class SmsCouponProductRelation(BaseObj):
			""" None"""
			def __init__(self,**kwargs):
				self.couponId = None
				self.id = None
				self.productId = None
				self.productName = None
				self.productSn = None
				super(CreateCouponApi.Body.SmsCouponProductRelation, self).__init__(**kwargs)

	class Resp(object):
		def __init__(self):
			super(CreateCouponApi.Resp, self).__init__()
			self.code = None
			self.data = None
			self.message = None



# api_obj = CreateCouponApi().set_token().send_request()
# print(api_obj.resp.__dict__)




















