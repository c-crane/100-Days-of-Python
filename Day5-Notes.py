## for loop with python lists
# Syntax: for item in list_of_items:
# Do something
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " " + "Pie")

# The range() function
# Syntax: for number in range(start, stop, step):
# Do something
for number in range(1, 11, 3):
  print(number)

total = 0
for number in range(1, 101):
  total += number
print(total)
  