import sys
import re

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    print("No file name provided.")
    sys.exit(1)

copies = {}
total = 0

with open(file_name, 'r') as file:
    for line in file:
        line = line.strip()
        colon_split = line.split(':')
        #id = colon_split[0].split(' ')[1].strip()
        id = re.search(r'\d+', colon_split[0]).group()
        numbers = colon_split[1].replace('  ', ' ').split('|')
        
        winning_numbers = numbers[0].strip().split(' ')
        my_numbers = numbers[1].strip().split(' ')

        matching_numbers = set(winning_numbers).intersection(my_numbers)

        number_of_matching_numbers = len(matching_numbers)
        #print("card", id, "had", number_of_matching_numbers, "matching numbers.")

        # add copies
        for i in range(1,number_of_matching_numbers+1):
            #print("add Card ", int(id)+i)
            copies[int(id)+i] = copies.get(int(id)+i, 0) + 1
        
        #print(copies)

        # process copies
        number_of_copies = copies.get(int(id), 0)
        #print("card", id, "had", number_of_copies, "copies.")
        
        for i in range(1,number_of_matching_numbers+1):
            #print("add Card ", int(id)+i)
            copies[int(id)+i] = copies.get(int(id)+i, 0) + number_of_copies

        print("total number of card ", id, "is", number_of_copies + 1)
        total += number_of_copies + 1
        
print("total number of cards is", total)