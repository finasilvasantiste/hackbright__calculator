"""Math functions for calculator."""

import arithmetic

wants_to_play = True

while wants_to_play:

    user_input = input("What would you like to compute? (To exit, type 'q'.)")
    user_input_split = user_input.split(" ")
    if user_input_split[0] == "q":
        wants_to_play = False
    else:
        print("inside else")
        if user_input_split[0] == "add":
            print("Adding")

            x = int(user_input_split[1])
            y = int(user_input_split[2])

            print(arithmetic.add(x, y))

        elif user_input_split[0] == "sub":
            print("Adding")

            x = int(user_input_split[1])
            y = int(user_input_split[2])

            print(arithmetic.subtract(x, y))


