


from lesson4.base import BaseObj
from  lesson4.part3.auth import auth_token
from lesson4.part3.RequestUtil import RequestUtil



class OrderManageCreate(RequestUtil):
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
			self.count = None  # 数量
			self.id = None  # None
			self.memberLevel = None  # 可领取的会员类型：0->无限时
			self.receiveCount = None  # 领取数量
			self.useCount = None  # 已使用数量
			super(OrderManageCreate.Body, self).__init__(**kwargs)

		class SmsCouponProductCategoryRelation(BaseObj):
			""" None"""
			def __init__(self,**kwargs):
				self.couponId = None
				self.id: None
				self.parentCategoryName = None
				self.productCategoryId = None
				self.productCategoryName = None
				super(OrderManageCreate.Body.SmsCouponProductCategoryRelation, self).__init__(**kwargs)

		class SmsCouponProductRelation(BaseObj):
			""" None"""
			def __init__(self,**kwargs):
				self.couponId = None
				self.id = None
				self.productId = None
				self.productName = None
				self.productSn = None
				super(OrderManageCreate.Body.SmsCouponProductRelation, self).__init__(**kwargs)

	class Resp(object):
		def __init__(self):
			super(OrderManageCreate.Resp, self).__init__()
			self.code = None
			self.data = None
			self.message = None


	def set_token(self):
		self.update_headers(dict(Authorization=auth_token))
		return self



api_obj = OrderManageCreate().set_token().send_request()
# print(api_obj.resp.__dict__)




















