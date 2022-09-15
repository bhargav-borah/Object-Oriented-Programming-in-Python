import csv

class Item:
	
	pay_rate = 0.8 #This is a class attribute
	all = []

	def __init__(self, name: str, price: float, quantity = 0):  #We don't need to specify a data type for quantity as it already has an int default value
		
		#Run validations for received arguments
		assert price >= 0, f"Price {price} not greater than or equal to 0"
		assert quantity >= 0, f"Quantity {quantity} not greater than or equal to 0"

		#Assign to self objects
		self.__name = name            
		self.price = price
		self.quantity = quantity
		#The above three are instance attributes, pay_rate is a class attribute

		#Adding this instance to 'all' list
		Item.all.append(self)

	#Property decorator = Read only atrribute
	@property
	def name(self):
		return self.__name # We add a double underscore here to prevent error when self._name = name is executed (see the __init__ constructor)

	@name.setter
	def name(self, value):
		if len(value) > 10:
			raise Exception("Name is too long!")
		
		self.__name = value

	def calculate_total_price(self):
		return self.price * self.quantity

	def apply_discount(self):
		self.price = self.price * self.pay_rate  #Item.pay_rate also works

	def __repr__(self):   #Used to decide the way Item.all will be represented
		return f"{self.__class__.__name__}({self.__name}, {self.price}, {self.quantity})" 

	"Class methods are used when they have something to do with the class, but mostly they are used to instantiate objects from structures of data"
	@classmethod
	def instantiate_from_csv(cls):
		with open('items.csv', 'r') as f:
			reader = csv.DictReader(f)
			items = list(reader)

		# for item in items:
		# 	print(item)

		for item in items:
			Item(
				name = item.get('name'),
				price = float(item.get('price')),
				quantity = int(item.get('quantity'))
			)

	#Static method should do something that has a relationship with the class, but not something that must be unique per instance
	@staticmethod
	def is_integer(num):
		if isinstance(num, float):
			return num.is_integer() #Count out floats that are point zero
		elif isinstance(num, int):
			return True
		else:
			return False

	# @property
	# def read_only_name(self):
	# 	return "AAA"
	