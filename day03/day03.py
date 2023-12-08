import sys
import string

ascii_symbols = string.printable.replace('.', '').replace(string.ascii_letters, '').replace(string.digits, '').replace(string.whitespace, '') # symbols that are not letters or digits, or '.' (period)
print(ascii_symbols)

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    print("No file name provided.")
    sys.exit(1)

schematic = []

with open(file_name, 'r') as file:
    part_numbers = []
    for line in file:
        schematic += [list(line)]

#print(schematic)

def find_adjacent_cells(matrix, i, j): # finds adjacent cells to a cell
    adjacent_cells = []
    rows = len(matrix)
    cols = len(matrix[0])

    # Check top cell
    if i > 0:
        adjacent_cells.append((i - 1, j))

    # Check bottom cell
    if i < rows - 1:
        adjacent_cells.append((i + 1, j))

    # Check left cell
    if j > 0:
        adjacent_cells.append((i, j - 1))

    # Check right cell
    if j < cols - 1:
        adjacent_cells.append((i, j + 1))

    # Check top-left cell
    if i > 0 and j > 0:
        adjacent_cells.append((i - 1, j - 1))

    # Check top-right cell
    if i > 0 and j < cols - 1:
        adjacent_cells.append((i - 1, j + 1))

    # Check bottom-left cell
    if i < rows - 1 and j > 0:
        adjacent_cells.append((i + 1, j - 1))

    # Check bottom-right cell
    if i < rows - 1 and j < cols - 1:
        adjacent_cells.append((i + 1, j + 1))

    return adjacent_cells

def is_symbol(matrix, i, j): # checks if a cell is a symbol
    char = matrix[i][j]
    return char in ascii_symbols

i = 0
for line in schematic:
    adj = False
    part = ""
    j = 0
    for c in line:
        if c in string.digits:
            part += c
            for cell in find_adjacent_cells(schematic, i, j):
                if is_symbol(schematic, cell[0], cell[1]):
                    adj = True

        elif c == '.' or c in ascii_symbols or c == '\n':
            if len(part) > 0:
                #print(part)
                for cell in find_adjacent_cells(schematic, i, j-1):
                    if is_symbol(schematic, cell[0], cell[1]):
                        adj = True
                if adj:
                    part_numbers.append(part)
                part = ""
                adj = False
        j += 1
    i += 1
            
print(part_numbers)
sum = 0
for part in part_numbers:
    sum += int(part)

print(sum)