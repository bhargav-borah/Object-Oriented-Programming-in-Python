from item import Item
# from phone import Phone

# Item.instantiate_from_csv()
# print(Phone.all)

from item import Item

item1 = Item("MyItem", 750)

# print(item1.read_only_name)

# item1.read_only_name = "BBB" #This line causes an error as it tries to change the value of a property

print(item1.name)
# item1.name = "OtherItem" #Error if @name.setter is not implemented

item1.name = "Other Items"
print(item1.name)

print(item1.name)





