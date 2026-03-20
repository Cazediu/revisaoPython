with open('manipulação de arquivos/teste.txt','w', encoding ='utf-8') as arquivo:

    arquivo.write("Primeira Linha\n")
    arquivo.write("Segunda Linha\n")

with open('teste.txt','a', encoding='utf-8') as arquivo:

    arquivo.write("Terceira Linha\n")
    arquivo.write("Quarta Linha\n")