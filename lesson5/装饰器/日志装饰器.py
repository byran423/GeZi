def outer(a):
	def func_wapper(func):
		def inner(*args, **kwargs):
			print("装饰之前----")
			if a == "info":
				print("----info-----")
				res = func(*args, **kwargs)
			elif a == "debug":
				print("----debug-----")
				res = func(*args, **kwargs)
			elif a == "error":
				print("----error-----")
				res = func(*args, **kwargs)
			elif a == "Critical":
				print("----Critical-----")
				res = func(*args, **kwargs)
			else:
				print("bug级别错误")


			print("装饰之后----")
			return res
		return inner
	return func_wapper

@outer("jjj")
def func():
	print("业务方法")

func()








