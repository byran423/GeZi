

from lesson4.part3.RequestUtil import RequestUtil


class Adminlogin(RequestUtil):
	def __init__(self,**kwargs):
		super().__init__()
		self.info = "登录以后返回token"
		self.host = "http://144.34.200.237:8080"
		self.url = "/admin/login"
		self.method = "post"
		self.body = self.Body(**kwargs)
		self.resp = self.Resp()

	class Body(object):
		def __init__(self, **kwargs):

			self.username = "admin"
			self.password = "macro123"

	class Resp(object):
		def __init__(self):
			super(Adminlogin.Resp, self).__init__()
			self.code = None
			self.data = self.Token()
			self.message = None

		class Token(object):
			def __init__(self):
				self.token = None
				self.tokenHead = None

