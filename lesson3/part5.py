

from lesson3.base import BaseObj


class ConsAnimalType:
	Cat = "猫"
	Dog = "狗"

class ConsPetShop:
	A = "A pet shop"
	B = "B pet shop"
	C = "C pet shop"


class Animal(BaseObj):
	"""
	类说明
	"""
	pet_shop = ConsPetShop.A


	def __init__(self,name,age,type,**kwargs):
		super.__init__(**kwargs)
		self.name = name
		self.age - age
		self.type - type
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
	def __init__(self,name,age):
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

print(cat.pet_shop,"+",dog.pet_shop)

Animal.pet_shop = ConsPetShop.B
cat_new = Cat(name="咖啡", age=2)
print(cat.pet_shop, "+", dog.pet_shop)






























