#A place holder can also include a modifier to format the value

#A modifier is included by adding a colon : follwed by a legal formatting type
#Like .2f which means fixed point number 2 decimal

#Display the price with 2 decimal

price =  59
ixt = f"The price is {price:.2f} dolars"
print(ixt)

#Display the values 95 with 2 decimal..we can also add values directly without keeping variable

txt = f"The price is {34:.2f} dollars"
print(txt)

#Perform operations in F - string

#Perform a math operation in the placeholder and return the result

tx = f"The price is {10 * 20} rupees"
print(tx)

pr = 59
tax = 0.25
t = f"The price is {pr + (pr * tax)} rupees"
print(t)