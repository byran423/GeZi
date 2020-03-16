







from threading import Thread,current_thread,enumerate
import time


def func1(a):
	print("start",a)
	time.sleep(1)
	print ("end",a)




if __name__ == '__main__':
	th = []
	for i in range(10):
		t1 = Thread(target=func1,args=(i,))
		t1.start()
		th.append(t1)

	for j in th:
		j.join()


	print("所有线程都结束了,{}".format(str(enumerate())))


