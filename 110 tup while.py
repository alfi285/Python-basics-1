# Using while loop

#You can loop through the tuple items by using a while loop

# Use the len() function to determine the length of the tuple
# then start at 0 and loop your way through the tuple items by reffering to their indexes

#Remember to increase the index by 1 after each iteration

#Print all items using a while loop to go through all the index numbers

fr = ("apple", "mango", "cherry", "grapes", "lemon")
i = 0
while i < len(fr):
    print(fr[i])
    i = i +1