#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty level: Type 'easy' or 'hard': ").lower()

attempts = 0

if level == 'easy':
  attempts = 10
elif level == 'hard':
  attempts = 5

answer = random.randint(1, 100)

guess = int(input("Make a guess: "))

while attempts > 0:
  print(f"You have {attempts} attempts remaining.")
  if guess > answer:
    print("Too high.")
    attempts -= 1
  elif guess < answer:
    print("Too low.")
    attempts -= 1
  else:
    print(f"You got it! The answer was {answer}.")
    break
  guess = int(input("Make a guess: "))


if attempts <= 0:
  print(f"You ran out of attempts. The answer was {answer}.")