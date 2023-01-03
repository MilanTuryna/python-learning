num = 100
arrNumber = [int(x) for x in str(num)]
ciphres = len(arrNumber)
sumCiphres = 0

prime = False   
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            prime = True
            break

for x in arrNumber:
    sumCiphres += x

print("V daném čísle je počet cifer:", ciphres)
print("Pokud sečteme cifry, dostaneme:", sumCiphres)
print("Je číslo prvočíslo?", "ano" if prime else "ne")
