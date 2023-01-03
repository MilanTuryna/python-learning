n = 350
fromNumber = 1

array = []
i = 0
while(i <= n):
    array.append(i)
    i += 1

for index, x in enumerate(array):
    stringNum = str(x)
    reversedNum = int(stringNum[::-1])
    array[index] = reversedNum

print(array)
