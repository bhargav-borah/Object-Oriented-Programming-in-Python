from item import Item

class Phone(Item): #class Phone inherits from class Item
				   #Phone -> Child class ; Item -> Parent class

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
