#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end

print("Welcome to the Band Name Generator.")
city = input("What city did you grow up in?\n")
# print(city)
pet_name = input("What is your pet's name?\n")
# print(pet_name)
your_band_name = city + " " + pet_name
print("Your band name is: " + your_band_name)