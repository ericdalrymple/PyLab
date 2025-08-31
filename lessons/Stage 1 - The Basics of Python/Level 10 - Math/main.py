# =============================== #
# ======= LESSON 10: Math ======= #
# =============================== #

# You can tell the computer to do math using VARIABLES and numbers.

# First, let's ask the player for a few numbers
a = input("Enter a number: ")
b = input("Enter another number: ")

# Turn the player's answers into numbers instead of text
a = int(a)
b = int(b)

# Add      (+): Add 'a' and 'b' and save the result in the 'sum' VARIABLE
sum = a + b

# Subtract (-): Subtract 'b' from 'a' and save the result in the 'difference' VARIABLE
difference = a - b

# Multiply (*): Multiply 'a' by 'b' and save the result in the 'product' VARIABLE
product = a * b

# Divide   (/): Divide 'a' by 'b' and save the result in the 'division' VARIABLE
division = a / b

# Let's print our results
print("sum:       ", a, "+", b, "=", sum)
print("difference:", a, "-", b, "=", difference)
print("product:   ", a, "*", b, "=", product)
print("division:  ", a, "/", b, "=", division)
