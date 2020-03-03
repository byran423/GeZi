from lesson4.part3.RequestUtil import RequestUtil
from lesson4.part3.auth import auth_token


class BaseOrderManageService(RequestUtil):
	def __init__(self):
		super().__init__()
		self.host = "http://144.34.200.237:8080"



	def set_token(self):
		self.update_headers(dict(Authorization=auth_token))
		return self










