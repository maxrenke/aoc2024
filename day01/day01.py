import sys


if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    print("No file name provided.")
    sys.exit(1)

with open(file_name, 'r') as file:
    values = []
    for line in file:
        # Process each line here
        digits = ''.join(filter(str.isdigit, line))
        length = len(digits)
        
        first = digits[0]
        last = digits[length - 1]

        value = (str(first) + str(last))
        values.append(value)

sum = 0
for v in values:
    #print(v)
    sum += int(v)

print(sum) 