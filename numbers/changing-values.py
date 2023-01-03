#Je dáno pole celých kladných čísel a dvě vstupní hodnoty - první číslo na vstupu mi určí, jaká čísla z pole nahradím číslem z druhého vstupu.
array =[54,75,11,4,5,1,4,541,3244,51,47441]
a = 54
b = 51
i = 0
while(i < len(array)):
    if(array[i] == a):
        array[i] = b
    i+=1
print(array)
