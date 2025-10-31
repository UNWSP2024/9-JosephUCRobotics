# Author: Joseph Kracht
# Last Modified: 10/31/2025
# Title: Average Numbers

# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.

# The program should handle the following exceptions:

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file
# are converted to a number.
def sum_numbers_from_file():
    try:
        # Open the names.txt file
        file = open('numbers.txt', 'r')

        # Read the first name
        number = file.readline()

        # Set the sum var to 0
        sum_of_numbers = 0

        # Set the error var to false
        error_converting_text_to_number = False

        # loop through all the numbers and add the number to the sum var each time
        while number != "":
            try:
                sum_of_numbers += float(number)
            except:
                error_converting_text_to_number = True
            number = file.readline()


        # display the sum
        if error_converting_text_to_number:
            print("Error: One or more lines in the numbers.txt file cannot be converted to a number.")
        print("The sum of all of the numbers in the in the numbers.txt file is", sum_of_numbers)

        # close the file
        file.close()
    except:
        print("There was an error reading the numbers.txt file.")

# You don't need to change anything below this line:
if __name__ == '__main__':
        sum_numbers_from_file()
