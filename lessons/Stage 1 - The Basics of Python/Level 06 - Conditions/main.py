# =================================== #
# ======= LEVEL 6: Conditions ======= #
# =================================== #

# A CONDITION is when we ask the computer a 'yes' or 'no' question. The computer will
# answer with 'True' if the answer is 'yes' and 'False' if the answer is 'no'.

# For example, we can ask the computer to compare VALUES in different ways:
#   'a == b' (is a equal to b?)
#   'a != b' (is a not equal to b?)
#   'a > b'  (is a bigger than b?)
#   'a >= b' (is a bigger or equal to b?)
#   'a < b'  (is a smaller than b?)
#   'a <= b' (is a smaller or equal to b?)
#
# When we ask the computer to compare VALUES this way, it will answer us with 'yes' (True) or 'no' (False).


# Let's look at some examples by asking the player for some values.
a = input("Type a number: ")
b = input("Type a number to compare: ")

# We need to transform the player's answers into numbers instead of text.
a = int(a)
b = int(b)

# Ask if 'a' and 'b' are equal and save the answer in the 'equals' VARIABLE
equals = a == b

# Ask if 'a' and 'b' are not equal and save the answer in the 'not_equals' VARIABLE
not_equals = a != b

# Ask if 'a' is bigger than 'b' and save the answer in the 'is_bigger' VARIABLE
is_bigger = a > b

# Ask if 'a' is smaller than 'b' and save the answer in the 'is_smaller' VARIABLE
is_smaller = a < b

# Print the answers saved in the VARIABLES above
print()
print("== | Is", a, "equal to", b, "?  ", equals)
print("!= | Is", a, "not equal to", b, "?  ", not_equals)
print(">  | Is", a, "bigger than", b, "?  ", is_bigger)
print("<  | Is", a, "smaller than", b, "?  ", is_smaller)
print()
