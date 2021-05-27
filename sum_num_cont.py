#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 27, 2021
# This program adds a bunch of numbers depending on
# the users input


# main func
def main():

    # find out how many numbers the user wants to enter
    num_of_nums_str = input("how many numbers do you want to add: ")

    # make sure the users input can be an integer
    try:
        num_of_nums = int(num_of_nums_str)

        # set these to 0
        counter = 0
        num_sum = 0

        # Tell the user that the numbers must be whole
        print("Numbers must be whole numbers or they will not be added")

        # actual code ###
        while (counter < num_of_nums):
            user_num = input("Input a number: ")

            try:
                # make sure the users input can be a number
                user_num = int(user_num)

                # add to the counter to prevent an infinite loop
                counter = counter + 1

                # if the number is not whole continue
                if(user_num % 1 != 0 or user_num < 0):
                    continue

                # add the users num to the sum
                num_sum = num_sum + user_num

            # if it cant be a number
            except ValueError:
                print("input must be a number")

        # print the result to the user
        print(num_sum)

    # if it cant be a number
    except ValueError:
        print("Not valid input")


# calls the main func
if __name__ == "__main__":
    main()
