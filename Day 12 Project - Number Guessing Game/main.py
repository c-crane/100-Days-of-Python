# Number Guessing Game

import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
mode = input("Choose a difficulty. Type 'easy' or 'hard': ")

num_guesses = 0
if mode == "easy":
  num_guesses = 10
elif mode == "hard":
  num_guesses = 5

number = random.randint(1, 100)
# print(number)

while num_guesses != 0:
 
  print(f"You have {num_guesses} attempts remaining to guess the number.")
  num_guesses -= 1
  guess = int(input("Make a guess: "))
  
  if num_guesses == 0 and guess != number:
    print(f"You lose! The number was {number}.")
    break
  if guess == number:
    print(f"You got it! The correct answer was {number}.")
    break
  elif guess > number:
    print("Too high.")
    print("Guess again.")
  elif guess < number:
    print("Too low.")
    print("Guess again.")


    

  