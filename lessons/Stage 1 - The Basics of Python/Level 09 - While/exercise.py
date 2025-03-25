# ================================================================================================== #
# EXERCISE:
#
#   Let's change the guessing game from our example. Pick two secret numbers instead of one, and
#   ask the player to guess a number that is between them.
#
# ================================================================================================== #

# Save two secret numbers in VARIABLES
secret_number = 11

# There is no guess yet, so we can set correct_guess as 'False'
correct_guess = False

# Repeat the instructions until the player makes a correct guess.
while not correct_guess:

    # Ask the player to guess and turn the player's guess into a number
    player_guess = input("Guess the secret number: ")
    player_guess = int(player_guess)

    # Ask the computer if the player's guess is equal to the secret number and save the answer in the 'correct_guess' VARIABLE.
    

    # If the guess is correct, we should congratualte the player.
    if correct_guess:
        print("You guessed correctly! Congratulations!")


    # Ask the computer if the player's guess is NOT equal to the secret number and save the answer in the 'wrong_guess' VARIABLE.
    wrong_guess = player_guess != secret_number

    # If the guess is wrong, we should tell the player.
    if wrong_guess:
        print("You guessed wrong. Please try again.")

