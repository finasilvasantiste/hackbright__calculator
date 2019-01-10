"""Math functions for calculator."""

import arithmetic

wants_to_play = True

while wants_to_play:

    user_input = input("What would you like to compute? (To exit, type 'q'.)")
    user_input_split = user_input.split(" ")
    if user_input_split[0] == "q":
        wants_to_play = False
    else:
        x = int(user_input_split[1])
        if len(user_input_split) == 3:
            y = int(user_input_split[2])
        elif len(user_input_split) == 4:
            y = int(user_input_split[2])
            z = int(user_input_split[3])

        if user_input_split[0] == "+":
            print("Adding")

            print(arithmetic.add(x, y))

        elif user_input_split[0] == "-":
            print("Subtracting")

            print(arithmetic.subtract(x, y))

        elif user_input_split[0] == "*":
            print("Multiplying")

            print(arithmetic.m(x, y))



