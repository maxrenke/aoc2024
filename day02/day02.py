import sys

colors = {('red',12), ('green',13), ('blue',14)}

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
        #print(id)

        rounds = right.split(';')
        #print(rounds)

        possible = 1
        for round in rounds:
            
            x = round.strip().replace(",","").split(' ')
            l = len(x)
            my_dict = {}  # Renamed the variable to avoid shadowing the built-in dict type

            for i in range(0, len(x), 2):
                my_dict[x[i+1]] = x[i]  # Assign the value to the string index
  
            #print(my_dict)
            for key in colors:
                if key[0] in my_dict:
                    if int(my_dict[key[0]]) > key[1]:
                        possible = 0
            
            
            
        if possible == 1:
            sum += int(id)
        
    print(sum)
            