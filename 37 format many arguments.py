# The format() method takes unlimited  numbers of arguments,

# Use the format() method to insert numbers into strings:

itemNo = 23
itemPrice = 500
itemQuantity = 100

myOrder = "I want {} items of item number {} for {} rupess"
print(myOrder.format(itemQuantity,itemNo,itemPrice))