# ================================================ #
# ======= LEVEL 7: Using 'if' Instructions ======= #
# ================================================ #

# Sometimes we want the instructions of the program to only happen sometimes. We can
# use the 'if' instruction to do this. The instructions after the 'if' instruction
# will only work if the condition is 'True'.

# For example, we will ask the player to guess a secret number, but we
# only say congratulations if they guess the right number.

# Save a secret number in a VARIABLE
secret_number = 11

# Ask the player to guess and turn the player's guess into a number
player_guess = input("Guess the secret number: ")
player_guess = int(player_guess)

# Ask the computer if the player's guess is equal to the secret number and save the answer in the 'correct_guess' VARIABLE.
correct_guess = player_guess == secret_number

# If the guess is correct, we should congratualte the player.
if correct_guess:
    print("You guessed correctly! Congratulations!")


# Ask the computer if the player's guess is NOT equal to the secret number and save the answer in the 'wrong_guess' VARIABLE.
wrong_guess = player_guess != secret_number

# If the guess is wrong, we should tell the player.
if wrong_guess:
    print("You guessed wrong. Please try again.")



# ================================================================================================== #
# EXERCISE:
#
#   Change this guessing game. Pick two secret numbers instead of one, and ask the player to
#   guess a number that is between them.
#
# ================================================================================================== #


