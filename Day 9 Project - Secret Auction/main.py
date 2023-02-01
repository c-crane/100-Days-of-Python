from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)


new_bid = "yes"
# Empty list to store dictionaries
bidders = []
#While loop that runs as long as there are other bidders
while new_bid != "no":
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  new_bid = input("Are there any other bidders? Type 'yes or 'no:\n")
  
  new_dict = {} #Empty dictionary to store name and bid 
  new_dict["name"] = name #Saves name input to key name "name" in dictionary
  new_dict["bid"] = bid #Saves bid input to key name "bid" in dictionary
  bidders.append(new_dict) #Adds each dictionary to the bidders list
  clear()

key = "bid"
highest_value = -1000000
#Finds the highest bid in the bidders list of dictionaries by comparing the "bid" values
for nested_dict in bidders:
    if key in nested_dict:
        value = nested_dict[key]
        if value > highest_value:
            highest_value = value

#Finds the winner by finding the name associated with the highest bid
winner = None
for nested_dict in bidders:
  if nested_dict["bid"] == highest_value:
    winner = nested_dict["name"]
    break

if new_bid == "no":
    print(f"The winner is {winner} with a bid of ${highest_value}")




