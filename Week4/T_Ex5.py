# Generate a random number from a given interval and ask the user to guess the number.
# Then check if the answer is correct.
import random

x = random.randint(1, 2)
y = int(input("Please enter a number between 1 and 10:"))

print(f"The randomly generated number is {x}.")

if x == y:
    print("Congratulations! You guessed the number correctly!")
else:
    print("Sorry! Try again!")
