# ============================================= #
# ======= LEVEL 8: Conditions Continued ======= #
# ============================================= #

# We can combine CONDITIONS to make bigger CONDITIONS with 'and', 'or', and 'not' when
# we need to ask the computer more complicated questions. Let's look at these
# new words
#
# CONDITION_1 and CONDITION_2   (are CONDITION_1 and CONDITION_2 both 'True'?)
#
# CONDITION_1 or CONDITION_2    (are either CONDITION_1 or CONDITION_2 'True'?)
#
# not CONDITION_1               (is CONDITION_1 not 'True'?)
#
# Let's see this in action!


print("You are walking down a road and you see two objects on the ground, but you can only carry one. Which one do you pick up?")
print("1 - Apple")
print("2 - Stick")

object_choice = input("Which do you choose? (Type the number): ")

print()

print("You continue to walk and you come to a fork in the road. Which direction do you take?")
print("1 - Left")
print("2 - Right")

direction_choice = input("Which do you choose? (Type the number): ")

has_apple = object_choice == "1"
has_stick = object_choice == "2"

went_left = direction_choice == "1"
went_right = direction_choice == "2"

print()

if has_apple and went_left:
    print("You find a horse and feed it the apple. It lets you ride it and you become lifelong friends.")


if has_apple and went_right:
    print("You see a bag hanging from a tree branch, but you can't reach it. You eat your apple and keep walking.")


if has_stick and went_left:
    print("You see a horse, but it's timid and walks away from you. You go on your way with your trusty walking stick and your journey is easier.")


if has_stick and went_right:
    print("You see a bag hanging from a tree branch and use the stick to reach it. Inside it, you find an orb that lets you see the future.")
