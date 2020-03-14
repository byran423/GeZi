

# class Decorater(object):
# 	def __init__(self, func):
# 		print("=------")
# 		self.func = func
#
# 	def __call__(self, *args, **kwargs):
# 		return self.func
#
#
# @Decorater
# def func():
# 	print("业务方法")
#


# func = func()
# func()


class Demo(object):
	def __init__(self, a):
		self.a = a

	def __call__(self, func):

		def inner(*args, **kwargs):
			if self.a == 1:
				print("1111----")
			else:
				print("222-----")
			func(*args, **kwargs)

		return inner

@Demo(1)
def demo():
	print("demo")

demo()


