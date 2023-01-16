"""
Optional bonus. See course site for details.

"""
"""
    Jordan Wheeler 
    15 January 2023
    This module is similar to rock paper scissors but with animals.
    Users will input their choice of animal and the computer will use a
    random generator. The inputs will compare to see who wins.
    """

# Change the name below to a name of your choice

import random
name = "Jeph"

# Fix the code below to print the name using an f-string

print()
print(f"Hello, I'm {name}, your gamebot.")
print(f"Let's play an animal guessing game!")
print(f"There are 3 animals: wolf, eagle, snake (a Python of course).")
print(f"The wolf scares the eagle.")
print(f"The eagle grabs the snake.")
print(f"The snake bites the wolf.")
print(f"I'll pick one and you pick one and we'll see who wins.")
print()
x = "wolf"
y = "eagle"
z = "snake"

# Winning order
winning_order = x > y, y > z, z > x

# Right now, the user choses wolf everytime.
# Modify the code so the user is asked to
# enter wolf, eagle, or snake.
# Hint: use the input() function
print("Pick from list")
user_choice = input({"wolf", "eagle", "snake"})

# Now the bot will pick one
buddy_choice = random.choice(["wolf", "eagle", "snake"])

# Report the choices
print()
print(f"You said {user_choice}.")
print(f"I said {buddy_choice}.")
print()


# Now we need to compare the choices and determine the winner
# Complete the logic to
# compare the choices and print who won
# In Python, indentation is important!
if user_choice == buddy_choice:
    print("We tied!")

if user_choice == x and buddy_choice == y:
    print("You Win!")
if user_choice == y and buddy_choice == z:
    print("You Win!")
if user_choice == z and buddy_choice == x:
    print("You Win!")
if user_choice == y and buddy_choice == x:
    print("I Win!")
if user_choice == z and buddy_choice == y:
    print("I Win!")
if user_choice == x and buddy_choice == z:
    print("I Win!")

# When you finish,
# right-click on the code and select "Format Document"

# Run the code, and play the game a few times.
# Copy the output from the terminal and paste it into
# a new file named xtra_p1out.txt.
