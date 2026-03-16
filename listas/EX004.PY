lista = []

for i in range (1,11):
    lista.append(i)

print(lista[0:4])
print(lista[7:10])

listaNova = []
while len(lista) > 0:
    
    if lista[0] % 2 != 0:
        listaNova.append(lista[0])
    lista.pop(0)

print(listaNova)
    
