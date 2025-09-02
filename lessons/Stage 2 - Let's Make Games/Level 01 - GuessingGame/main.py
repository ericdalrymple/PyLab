import random

# Pick a random number between 1 and 100
number = random.randint(1, 100)

# Make the player guess until they find the number. The 'while' instruction will repeat
# the code as long as the guess and the number are different (until the player guesses).
guess = 0
while guess != number:
    guess = int(input("Guess a number between %d and %d: "%(1, 100)))
    if guess < number:
        print("Higher!")
    else:
        print("Lower!")

print("Congratulations! You guessed the correct number! %d"%(number))
