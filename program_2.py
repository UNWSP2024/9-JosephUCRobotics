# Author: Joseph Kracht
# Last Modified: 10/30/2025
# Title: Random Number File Writer
import random

# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the file will hold
# (up to 1000).

input_is_valid = False
while not input_is_valid:
    try:
        number_of_random_numbers = int(input("How meany random numbers should I write to the random_numbers.txt file(int 1 to 1000): "))
        if number_of_random_numbers <= 0 or number_of_random_numbers > 1000:
            print("The number must be 1 through 1000")
        else:
            input_is_valid = True

    except:
        print("Invalid Input")

file = open('random_numbers.txt', 'w')

for i in range(number_of_random_numbers):
    number = random.randint(1,501)
    file.write(str(number) + "\n")
