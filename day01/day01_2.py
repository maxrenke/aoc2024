import sys
from collections import Counter


if len(sys.argv) > 1:
    file_name = sys.argv[1]
    left = []
    right = []

    with open(file_name, 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) == 2:
                left.append(int(columns[0]))
                right.append(int(columns[1]))

    right_counter = Counter(right)
    print("Right counter:", right_counter)
    
    print(sum(right_counter[l]*l for l in left ))

else:
    print("No file name provided.")
    sys.exit(1)