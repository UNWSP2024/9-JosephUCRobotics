# Author: Joseph Kracht
# Last Modified: 10/30/2025
# Title: Item Counter

# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    # Open the names.txt file
    file = open('names.txt', 'r')

    # Read the first name
    name = file.readline()

    # Set the counter var to 0
    number_of_names = 0

    # loop through all the names and add 1 to the counter each time
    while name != "":
        number_of_names += 1
        name = file.readline()

    # display the number of names
    print("There are", number_of_names, "names in the name.txt file")
    file.close()



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
