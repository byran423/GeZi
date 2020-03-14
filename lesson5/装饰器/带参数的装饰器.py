#
# import time
#
# def out(a):
# 	def func_wapper(func):
# 		print("---"*10)
# 		def inner(*args,**kwargs):
# 			s = time.time()
# 			if a == 1 :
# 				func(*args, **kwargs)
# 				print("操作耗时{}秒".format(str(time.time() - s)))
# 			else:
# 				time.sleep(2)
# 				print("等待2秒")
# 				func(*args, **kwargs)
# 				print("操作耗时{}秒".format(str(time.time() - s)))
# 		return inner
# 	return func_wapper
#
#
#
# @out(5)
# def func(a):
# 	print(a)


# func(11)
#

def login(name, passwd):
	if name == "admin" and passwd == "admin":
		print("login success!")
	else:
		print("login failed!")



a = {"name":"admin","passwd":"admin"}
b = {"name":"admin1","passwd":"admin"}
c = {"name":"admin","passwd":"admin1"}
d = {"name":"admin1","passwd":"admin1"}


# def param(tmp_list:list):
# 	def wapper_func(func):
# 		def inner(*args, **kwargs):
# 			res_tmp = []
# 			for i in tmp_list:
# 				res_tmp.append(login(name=i['name'], passwd=i['passwd']))
# 			return res_tmp
# 		return inner
# 	return wapper_func
#
#
# @param([a,b,c,d])
# def test5():
# 	pass
#
#
#
# a = test5()



class Newobject(object):
	def __init__(self):
		print("初始化")

	def __call__(self, *args, **kwargs):
		print("cccc")


obj = Newobject()
obj()




