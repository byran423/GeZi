def print_msg():
	msg = "I am a closure"
	def inner():
		print(msg)
	return inner


closure = print_msg()
closure()










