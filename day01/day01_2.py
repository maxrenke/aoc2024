import sys


if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    print("No file name provided.")
    sys.exit(1)

spelled = "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"

with open(file_name, 'r') as file:
    values = []
    for line in file:
        # Process each line here
        line = line.strip()
        print("line", line)
        built = ""
        digits = []
        for l in line:
            #print("l", l)
            built += l
            if l.isdigit():
                digits += l
                built = built[1:]
            else:
                for s in spelled:
                    if s in built: 
                        print("add", spelled.index(s) + 1)
                        digits += (str(spelled.index(s) + 1))
                        #built = built[(len(s)-1):] #remove first character to prevent duplicate adds
                        #break
                        
        
        print("digits", digits)
        length = len(digits)
        
        first = digits[0]
        last = digits[length - 1]
        print("first", first, "last", last)

        value = (str(first) + str(last))
        print("value", value, int(value))
        values.append(value)

        input()

sum = 0
for v in values:
    sum += int(v)

print(sum)