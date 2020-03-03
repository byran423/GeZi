from lesson4.part5.order_service.api.controller.CreateCouponApi import CreateCouponApi as TemplateController


class CouponCreateApiService(TemplateController):
	def __init__(self, status=200, message="操作成功", **kwargs):
		super().__init__()
		self.status = status
		self.message = message
		self.update_default_body(**kwargs)
		self.set_token()

	def get_coupon_info(self):
		self.coupon_info = None

	def update_dafault_body(self, **kwargs):
		self.body.amount = 299
		self.body.enableTime = "2019-11-30T16:00:00.000Z"
		self.body.minPoint = 10
		self.body.name = "优惠券测试"
		self.body.note = "备注信息"
		self.body.perLimit = 1
		self.body.platform = 0
		self.body.productCategoryRelationList = []
		self.body.productRelationList = []
		self.body.publishCount = 1000
		self.body.startTime = "2019-11-14T16:00:00.000Z"
		self.body.type = 0
		self.body.useType = 0
		self.body.update_value(**kwargs)

	# def add_cate_relation(self, **kwargs):
	# 	"""新增优惠券类型"""


















