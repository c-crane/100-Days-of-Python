# Random Module
import random # Allows us to use random module
import my_module

random_int = random.randint(1, 10) #random integer between 1 and 10
print(random_int)

print(my_module.pi)

random_float = random.random() * 5 # random between 0 and 1 multiplied by 5 to give random float between 0 and 5
print(random_float)

## Offset and Appending Items to Lists
# Lists are a data sctructure
# fruits = ["item1", item2]
# .append() to add item to end of list

## Nested Lists

# dirty_dozen = ["Strawberries", "Spinach","Kale","Nectarines","Apples","Grapes","Peaches","Cherries","Pears","Tomatoes","Celery","Potatoes"]

fruits = ["Strawberries","Nectarines","Apples","Peaches","Cherries","Pears","Grapes"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables] # Nested List
print(dirty_dozen)

# When inserting a new value you do the column first then the row, so:
# name_of_nested_list[column][row]