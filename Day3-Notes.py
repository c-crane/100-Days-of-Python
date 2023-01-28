## Control Flow with if/else and conditional operators
# Syntax
# if condition:
#   do this
# else:
#   do this
# Everything that is indented is inside that operator

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("Can ride")
else: 
  print("Can't ride")

## Comparison operators
# > greater than
# < less than
# >= greater than or eqaul to
# <= less than or equal to
# == equal to
# != not equal to
# % return the remainder

## Nested if/else statement
# Syntax:
# if condition: 
#   if another condition:
#     do this - in order for this to executet the outside and inside conditions must be met
#   else:
#     do this - for this to run the first condition will be true and second will be false
# else:
#   do this - will run if first statement is false

## elif (else/if)
#Syntax:
  # if condition1:
  #   do a
  # elif condition2:
  #   do b 
  # else: 
  #   do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("Can ride")
  age = int(input("What is your age?"))
  if age < 12:
    print("Please pay $5")
  elif age <= 18:
    print("Please pay $7")
  else:
    print("Please pay $12")
else: 
  print("Can't ride")

## Multiple if statements

# Syntax:
# if condition1:
#   do A 
# if condition2:
#   do B 
# if condition3:
#   do C - if all 3 are true then, A, B, and C will execute

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("Can ride")
  age = int(input("What is your age?"))
  if age < 12:
    bill = 5
    print("Please pay $5")
  elif age <= 18:
    bill = 7
    print("Please pay $7")
  else:
    bill = 12
    print("Please pay $12")

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
    print(f"Please pay ${bill}")
    
else: 
  print("Can't ride")

## Logical Operators
# and - both conditions must be true exectue
a = 12
a > 10 and a < 13
# or - one condition must be true
# not - reverses a condition (True to false/ False to true)
not a > 10 # returns false