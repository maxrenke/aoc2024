import sys

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    print("No file name provided.")
    sys.exit(1)

sum = 0

with open(file_name, 'r') as file:
    for line in file:
        line = line.strip()
        colon_split = line.split(':')
        id = colon_split[0].split(' ')[1].strip()
        numbers = colon_split[1].replace('  ', ' ').split('|')
        
        winning_numbers = numbers[0].strip().split(' ')
        my_numbers = numbers[1].strip().split(' ')

        matching_numbers = set(winning_numbers).intersection(my_numbers)

        points = 0
        if len(matching_numbers) > 0:
            points = 2 ** (len(matching_numbers)-1)

        print("id: ", id)
        #print("winning numbers: ", winning_numbers)
        #print("my numbers: ", my_numbers)
        #print("matching numbers: ", matching_numbers)
        print("points: ", points)

        sum += points

print("sum: ", sum)