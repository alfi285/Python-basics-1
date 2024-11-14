#You can perform if...else inside the placeholder

price =48
txt = f"It is very{'Expensive' if price>50 else 'cheap'}"

print(txt)

#We can use function...inside placeholder
fruit = "Apple"
txt = f"I love {fruit.upper()}"
print(txt)