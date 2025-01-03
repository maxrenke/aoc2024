import sys


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

                left.sort()
                right.sort()

    print("Left array:", left)
    print("Right array:", right)

    difference_sum = sum(abs(l - r) for l, r in zip(left, right))
    print("Sum of differences:", difference_sum)
else:
    print("No file name provided.")
    sys.exit(1)