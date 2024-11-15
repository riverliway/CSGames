
def letter_train(string, counter=0):
    for index in range(len(string)):
        counter = process_char(string, index, counter)
        
    return counter
        
def process_char(string, index, counter):
    print(string[index], counter)
    functions = {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "E": E,
        "F": F,
        "G": G,
        "H": H,
        "I": I,
        "J": J,
        "K": K
    }
    return functions[string[index]](string, index, counter)
    
def A(string, index, counter):
    return counter + 5

def B(string, index, counter):
    return counter * 2

def C(string, index, counter):
    s = str(counter)
    cumsum = 0
    for i in s:
        cumsum += int(i)
    return counter + cumsum

def D(string, index, counter):
    return process_char(string, index - 3, counter)

def E(string, index, counter):
    counter -= 13
    return letter_train("ABA", counter)

def F(string, index, counter):
    return len(str(counter))
    
def G(string, index, counter):
    for i in range(1, 4):
        counter = process_char(string, index - i, counter)
    return counter

def H(string, index, counter):
    new_counter = letter_train(string[index - 5:index])
    return counter + new_counter

def I(string, index, counter):
    options = [A, B, C]
    return options[counter % 3](string, index, counter)

def J(string, index, counter):
    cumsum = 0
    for i in range(1, 5):
        cumsum += ord(string[index - i])
    return counter + cumsum

def K(string, index, counter):
    options = [A, B, C, D, E, F, G, H, I, J, K]
    previous = ord(string[index - 1]) - ord('A')
    return options[(previous + 1) % len(options)](string, index - 1, counter)

string = "ABCEBGGJAGABBICHIIIGGGGDABCKBGGFABAAIGJHGAKBGGHEKAKIGGCKC"
counter = letter_train(string)
print(counter)