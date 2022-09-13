import csv

class Item:
	
	pay_rate = 0.8 #This is a class attribute
	all = []

	def __init__(self, name: str, price: float, quantity = 0):  #We don't need to specify a data type for quantity as it already has an int default value
		
		#Run validations for received arguments
		assert price >= 0, f"Price {price} not greater than or equal to 0"
		assert quantity >= 0, f"Quantity {quantity} not greater than or equal to 0"

		#Assign to self objects
		self.name = name            
		self.price = price
		self.quantity = quantity
		#The above three are instance attributes, pay_rate is a class attribute

		#Adding this instance to 'all' list
		Item.all.append(self)

	def calculate_total_price(self):
		return self.price * self.quantity

	def apply_discount(self):
		self.price = self.price * self.pay_rate  #Item.pay_rate also works

	def __repr__(self):   #Used to decide the way Item.all will be represented
		return f"Item({self.name}, {self.price}, {self.quantity})" 

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

	#Static method should do something that has a relationship with the class, but not somehting that must be unique per instance
	@staticmethod
	def is_integer(num):
		if isinstance(num, float):
			return num.is_integer() #Count out floats that are point zero
		elif isinstance(num, int):
			return True
		else:
			return False

	#Static methods don't pass the class as the class as the first argument in the argument, whereas class methods do
	#Static and class methods can be called not only from the class level, but also from the instance level, though it rarely makes sense to do so

Item.instantiate_from_csv() 
print(Item.all)

print(Item.is_integer(9.0))