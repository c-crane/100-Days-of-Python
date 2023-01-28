#Data Types

# String
print("Hello"[4]) # Can pull out individual characters with []

# Integer - numbers without decimals
print(110 + 100)
# Can replace commas with underscores for large numbers:
print(1_000_000_000)

#Float - numbers with decimals

# Check the type of data: type()

# Change the type of data:
num_char = len(input("What is your name?"))

new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")


# To use exponents use (**)
print(2**3)

## Number Manipulation and F Strings

# Rounding Numbers
print(round(8 / 3, 2)) # the 2 tells how many decimals you want to round to.and

#Floor division - only return whole number (//)
print(4 // 3)

#Updating variables
score = 0
#User scores a point
score += 1 # Can do for all other operations(- * /)
print(score)

#Multiple data types, use f-String
score = 0 
height = 1.8
isWinning = True
#f-String
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")