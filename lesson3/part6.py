

class AttrDict(dict):
	"""
	继承dict的所有用法，加以改造
	"""

	def __getattr__(self, attr):
		"""
		实现符号.取值
		"""
		try:
			return self[attr]
		except KeyError:
			raise AttributeError(attr)

	def __setattr__(self, attr, value):
		"""
		实现符号.赋值
		"""
		self[attr] = value


	def __add__(self, d):
		"""
		实现+计算符
		"""
		for k,v in d.item():
			if k in self:
				self.scroe += d.scroe
				break
		return self












