def evolution(population):
    newpop = list(population)
    for index in range(len(population)):
        left = "0" if index - 1 < 0 else population[index - 1]
        right = "0" if index + 1 >= len(population) else population[index + 1]
        
        if left == "0" and right == "0":
            newpop[index] = "0"
        elif left == "1" and right == "1":
            newpop[index] = "0"
        else:
            newpop[index] = "1"
        
    return "".join(newpop)

population = "01010011010110101110"
populations = [population]
day = 0

while True:
    day += 1
    newpop = evolution(population)
    if newpop in populations:
        break
    populations.append(newpop)
    population = newpop

print(populations)
print("stagnation on day", day)