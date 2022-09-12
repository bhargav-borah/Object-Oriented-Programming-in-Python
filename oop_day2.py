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

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# item1.has_quad_cam = False  # We can also add attributes in this way

# print(item1.name, item1.price, item1.quantity, item1.has_quad_cam)

# print(item1.calculate_total_price())

# print(Item.pay_rate)   #Accessing pay_rate class attribute from the class level

# print(item1.pay_rate)  #Accessing pay_rate class attribute from the instance level

# print(Item.__dict__) #All attributes at the class level
# print(item1.__dict__) #All attributes at the instance level

# item1.apply_discount()
# print(item1.price)

# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

print(Item.all)

# for instance in Item.all:
# 	print(instance.name)