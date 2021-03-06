

from lesson4.part4.RequestUtil import RequestUtil


class AdminLogin(RequestUtil):
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
			self.username = None
			self.password = None

	class Resp(object):
		def __init__(self):
			super(AdminLogin.Resp, self).__init__()
			self.code = None
			self.data = self.Token()
			self.message = None

		class Token(object):
			def __init__(self):
				self.token = None
				self.tokenHead = None

