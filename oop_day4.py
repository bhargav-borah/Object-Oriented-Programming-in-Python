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
		return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})" 

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

class Phone(Item): #class Phone inherits from class Item
				   #Phone -> Child class ; Item -> Parent class

	all = []
	# def __init__(self, name : str, price : float, quantity = 0, broken_phones = 0):

	# 	assert price >= 0, f"Price {price} is not greater than or equal to 0"
	# 	assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"
	# 	assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to 0"

	# 	self.name = name
	# 	self.price = price
	# 	self.quantity = quantity
	# 	self.broken_phones = broken_phones

	# 	Phone.all.append(self)

	def __init__(self, name : str, price : float, quantity = 0, broken_phones = 0):

		# Call to super() function to access all the attributes of the parent class
		super().__init__(
			name, price, quantity
		)

		assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to 0"

		self.broken_phones = broken_phones

		Phone.all.append(self)


# phone1 = Phone("jscPhonev10", 500, 5)
# phone1.broken_phone = 1

# phone2 = Phone("jscPhonev20", 700, 5)
# phone2.broken_phones = 1

# phone1 = Phone("jscPhonev10", 500, 5, 1)
# print(phone1.calculate_total_price())

# phone2 = Phone("jscPhonev20", 700, 5, 1)

phone1 = Phone("jscPhonev10", 500, 5, 1)


# We get the same output for the following 2 print statements as __repr__ function is defined in the Item class and inherited by the Phone class
# print(Item.all)
# print(Phone.all)

# After making changes to __repr__function
print(Item.all)
print(Phone.all)

# We can remove the all attribute (and the Phone.all.append(self) line) from the Phone class and we would still have the same output for the above 2 print statements, 
# as the all attribute of the parent class is already inherited


