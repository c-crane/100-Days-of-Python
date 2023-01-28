#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Get random letters
nr_letters= int(input("How many letters would you like in your password?\n")) 
rand_let = []
for letter in range(nr_letters):
  rand_let.append(random.choice(letters))
  if letter == nr_letters - 1:
    password1 = "".join(rand_let)
    # print(password1)
    break

# Get random symbols
rand_sym = []
nr_symbols = int(input(f"How many symbols would you like?\n"))
for symbol in range(nr_symbols):
  rand_sym.append(random.choice(symbols))
  if nr_symbols > len(symbols):
    print("You can only have 1 - 9 symbols.")
    break
  elif symbol == nr_symbols - 1:
    password2 = "".join(rand_sym)
    # print(password2)
    break

# Get random numbers
rand_num = []
nr_numbers = int(input(f"How many numbers would you like?\n"))
for number in range(nr_numbers):
  rand_num.append(random.choice(numbers))
  if nr_numbers > len(numbers):
    print("You can only have 1 - 10 numbers.")
    break
  elif number == nr_numbers - 1:
    password3 = "".join(rand_num)
    # print(password3)
    break

password = ''.join([password1, password2, password3])
password = list(password)
random.shuffle(password)
password = ''.join(password)
print(password)

