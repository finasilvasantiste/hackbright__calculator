"""Math functions for calculator."""

import arithmetic

user_input = input("What would you like to compute? ")

user_input_split = user_input.split(" ")

# for item in user_input_split:
#     print(item)

if user_input_split[0] == "add":
    print("Adding")

    x = int(user_input_split[1])
    y = int(user_input_split[2])

    print(arithmetic.add(x, y))




