import time

def func_wapper(func):
	print("---"*10)

	def inner(*args, **kwargs):
		s = time.time()
		res = func(*args, **kwargs)
		print("操作耗时{}".format(str(time.time()-s)))
		return res
	return inner





@func_wapper
def func(a):
	"""普通函数"""
	print(a)
	print("closure")

func(1)











