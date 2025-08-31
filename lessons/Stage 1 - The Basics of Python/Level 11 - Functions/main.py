# =================================== #
# ======= LESSON 11: Function ======= #
# =================================== #

# 'Functions' are instructions that you can write yourself using other
# instructions. Then you can give the computer that instruction later on.

# Some 'functions' can send back VALUES using the 'return' instruction, and
# others simply do something without sending back anything. Let's look at
# some examples.

# You can make a function using the 'def' instruction. Here we're making
# a function called 'do_something' that just prints a message.
def do_something():
    print("Here is the answer!")


# Here we're making a function that sends back the number 11.
def get_number():
    return 11


# Functions can be setup take VALUES. Here we're making a function
# that takes two numbers, multiplies them, and sends back the answer.
def multiply_numbers(a, b):
    return a * b


# Here we're making a function that takes two numbers, adds them,
# and send back the answer.
def add_numbers(a, b):
    return a + b


# ================================================================================================== #


# Up until here, the program still didn't do anything. We just created
# a bunch of functions. Now we will start using the functions we made.


# Use the 'get_number' function and save the number in the 'number' VARIABLE.
number = get_number()

# Use the 'multiply_numbers' function to multiply 'number' by 3 and save
# the answer in the 'm' VARIABLE.
m = multiply_numbers(number, 3)

# Use the 'do_something' function to print a message.
do_something()

# Write the answer!
print(m)
