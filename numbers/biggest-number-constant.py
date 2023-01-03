array = [45,74,8758,4565,2145,36225]
constant = 1000
maxNumber = 0
for x in array:
    if x > maxNumber AND x < constant:
        maxNumber = x
print("Největší číslo menší než 1000 je:", maxNumber)

