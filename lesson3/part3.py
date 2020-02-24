class ConsAnimalType:
	Cat = "猫"
	Dog = "狗"

class Animal(object):
	def __init__(self,name,type,age):
		"""

		:param name:
		:param type:
		:param age:
		:param owner:
		"""
		self.name = name
		self.age = age
		self.type = type
		self.eat_foods = []
		self.reason = "我今天忘记喂食"

	def eat(self, food):
		"""

		:param food:
		:return:
		"""
		if isinstance(food, str):
			self.eat_foods.append(food)
		else:
			print("它吃了不该吃的，呕吐了")
			self.eat_foods = []
			self.reason = "{}吃了{}生病了".format(self.name, str(food))
		return self

class Dog(Animal):
	def __init__(self,name,age,dog_type="宠物狗"):
		super().__init__(name=name,
						 age=age,
						 type=ConsAnimalType.Dog)

		self.dog_type = dog_type

	def can_run(self):
		print("狗会跑")


class Cat(Animal):
	def __init__(self,name,age,):
		super().__init__(name=name,
						 age=age,
						 type=ConsAnimalType.Cat)

	def can_jump(self):
		print("猫会跳")




my_animal = list()
# cat = Animal(name="凯斯", type=ConsAnimalType.Cat, age=1)
# dog = Animal(name="旺旺", type=ConsAnimalType.Dog, age=2)
cat = Cat(name="凯斯", age=1)
dog = Dog(name="旺旺", age=2)

cat.eat_foods.append("零食")
my_animal.append(cat)
my_animal.append(dog)


cat.eat("小鱼").eat("小鱼").can_jump()
# cat.eat("大鱼")
dog.eat("骨头").eat("狗粮")
dog.eat(1111)
dog.can_run()


def show_your_animal():
	for animal in my_animal:
		print("我有一只{tppe},它叫{name},{age}岁了".format(tppe=animal.type,
 												   name=animal.name,
												   age=animal.age))
		if animal.eat_foods:
			food_str = "、".join(animal.eat_foods)
			print("它今天吃了{}".format(food_str))
		else:
			print("它今天什么都没吃,因为{}".format(animal.reason))

show_your_animal()

































