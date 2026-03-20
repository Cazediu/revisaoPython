while True:

    produto = input("Escreva o produto: ")

    if produto != "Sair":
        with open('manipulação de arquivos/exercicios/compras.txt','w', encoding ='utf-8') as compras:

            compras.write(produto.strip())

    else:
        break

with open('manipulação de arquivos/exercicios/compras.txt','r', encoding ='utf-8') as compras:
    print(compras.read())

        

        
