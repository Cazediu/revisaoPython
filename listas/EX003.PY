numeros = [3, 17, 8, 42, 5, 100, 23, 66, 11, 99]

listaPar = []
for n in numeros:
    if n % 2 == 0:
        listaPar.append(n)
print(listaPar)

ListaMaior = []
for n in numeros:
    if n > 20:
        ListaMaior.append(n)
print(ListaMaior)

print(sum(numeros))