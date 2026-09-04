# Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number. After each guess the program prints out a text:
# Too high, Too low or Correct. Notice that the computer must not change the number between guesses.

import random
num=random.randint(1,10)
guess = 0
repeat=0
while  (guess!=num):
    guess= int(input("Guess the number: "))
    if guess <1 or guess>10:
        print("Out of range")
    elif guess<7:
        print("Too low")
    elif guess>7:
        print("Too high")
    elif guess==7:
        print("correct")
    repeat=repeat +1


