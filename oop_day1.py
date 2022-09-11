#item1 = 'Phone'
# item-price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity

class Item:
	#Methods = Functionn inside classes
	def calculate_total_price(self, x, y):
		return x * y

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(type(item1)) # __main__.Item
print(type(item1.name)) #str
print(type(item1.price)) #int
print(type(item1.quantity)) #int

print(item1.calculate_total_price(item1.price, item1.quantity)) #500