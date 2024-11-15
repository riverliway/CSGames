

input = [
    "HEYBROGUESSW",
    "HATTHISSAYSA",
    "COOLMESSAGEW",
    "HENYOUUNDOIT"
]

output = ['OXOAJHVMBEVX', 'LLVNVGSLKQPD', 'DODGDSPWIJQY', 'EDHVUFBXFTUH']

def shift_letter(letter, amount):
    i = ord(letter) - ord('A') + amount
    if i >= 26:
        i -= 26
    elif i < 0:
        i += 26
    return chr(i + ord('A'))

# Shifts each letter of the grid by an amount specified
# in the shiftings array
def shift(input, shiftings):
    output = []
    for row in range(len(input)):
        r = ""
        for col in range(len(input[0])):
            r += shift_letter(input[row][col], shiftings[row][col])
        output.append(r)
    return output

# Cycles each row by an amount
def cycle_row(input, shiftings):
    output = []
    for row in range(len(input)):
        l = len(input[row])
        i = shiftings[row] % l
        r = input[row][-(l - i):] + input[row][:i]
        output.append(r)
    return output
    
# Cycles each column by an amount
def cycle_col(input, shiftings):
    output = []
    for row in range(len(input)):
        r = ""
        for col in range(len(input[0])):
            c = (row + shiftings[col]) % len(input)
            r += input[c][col]
        output.append(r)
    return output

def swap_letters(list_input, x1, y1, x2, y2):
    temp = list_input[x1][y1]
    list_input[x1][y1] = list_input[x2][y2]
    list_input[x2][y2] = temp
    
def swap(input, swaps):
    list_input = [list(i) for i in input]
    
    for x1, y1, x2, y2 in swaps:
        swap_letters(list_input, x1, y1, x2, y2)
    
    return [compound(i) for i in list_input]

swap_list = [
    (3, 1, 1, 6),
    (2, 8, 0, 9),
    (1, 0, 0, 1),
    (3, 5, 2, 6),
    (0, 4, 1, 8)
]
def transform(input):
    output = shift(input, [[i + j for i in range(12)] for j in range(4)])
    output = cycle_row(output, [i + 3 for i in range(4)])
    output = cycle_col(output, [i for i in range(12)])
    output = swap(output, swap_list)
    output = cycle_col(output, [i * i + 33 for i in range(12)])
    output = shift(output, [[i * j for i in range(12)] for j in range(4)])
    
    return output
    
def transform_inverse(output):
    input = shift(output, [[-(i * j) for i in range(12)] for j in range(4)])
    input = cycle_col(input, [-(i * i + 33) for i in range(12)])
    input = swap(input, [(x2, y2, x1, y1) for x1, y1, x2, y2 in swap_list])
    input = cycle_col(input, [-i for i in range(12)])
    input = cycle_row(input, [-(i + 3) for i in range(4)])
    input = shift(input, [[-(i + j) for i in range(12)] for j in range(4)])
    
    return input

def compound(var):
    return "".join(var)
    
#output = transform(input)
#print(compound(output))

print(compound(transform(input)))
print(transform_inverse(output))
