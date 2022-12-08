maximal = int(input("Zadej maximální číslo, do které mám vypočítat fibonacciho posloupnost:"))
# an = an-1 + an-2
i = 2
array = [0,1]
while(i < maximal):
    array.append(array[i-1] + array[i-2])
    i +=1
print(array)
