with open('manipulação de arquivos/exercicios/frutas.txt','w', encoding ='utf-8') as frutas:

    frutas.write("Laranja\n")
    frutas.write("Banana\n")
    frutas.write("Maçã\n")
    frutas.write("Caju\n")
    frutas.write("Maracujá\n")

with open('manipulação de arquivos/exercicios/frutas.txt','r', encoding ='utf-8') as frutas:
    print(frutas.read())