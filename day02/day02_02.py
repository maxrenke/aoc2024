import sys

colors = {'red': 12, 'green': 13, 'blue': 14}

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    print("No file name provided.")
    sys.exit(1)

with open(file_name, 'r') as file:
    values = []
    sum = 0
    for line in file:
        # Process each line here
        line = line.strip()
        left = line.split(':')[0]
        right = line.split(':')[1]
        id = left.split(' ')[1]
        print(id)

        rounds = right.split(';')
        #print(rounds)

        my_dict = {}  # Renamed the variable to avoid shadowing the built-in dict type
        for round in rounds:
            
            x = round.strip().replace(",","").split(' ')
            l = len(x)
            

            for i in range(0, len(x), 2):
                if x[i+1] in my_dict:
                    if int(my_dict[x[i+1]]) < int(x[i]):
                        my_dict[x[i+1]] = x[i]  # Assign the value to the string index
                else:
                    my_dict[x[i+1]] = x[i]  # Assign the value to the string index
  
            for key in my_dict:
                colors[key] = my_dict[key]
        
        print(colors)
        
        power = 1
        for key in colors:
            power *= int(colors[key])
        sum += power

        print(power)

    print(sum)