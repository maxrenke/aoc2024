import sys


if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    print("No file name provided.")
    sys.exit(1)

#with open(file_name, 'r') as file: