
class ConsAnimalType:
	Cat = "猫"
	Dog = "狗"

class Animal(object):
	def __init__(self,name,type,age,owner=None):
		"""

		:param name:
		:param type:
		:param age:
		:param owner:
		"""
		self.name = name
		self.age = age
		self.type = type
		self.__owner = owner


my_animal = list()
cat = Animal(name="凯斯",type=ConsAnimalType.Cat,age=1,owner="YB")
dog = Animal(name="旺旺",type=ConsAnimalType.Dog,age=2)
cat.name = "喵喵"
my_animal.append(cat)
my_animal.append(dog)
cat.name = "凯斯"

def show_your_animal():
	for animal in my_animal:
		print("我有一只{type},它叫{name},它今年{age}岁了".format(type=animal.type,
													  name=animal.name,
													  age=animal.age))
		try:
			print("他的主人是{__owner}".format(animal.____owner))
		except Exception as e:
			print(e)

show_your_animal()








