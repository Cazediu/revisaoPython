#Cria um arquivo e adiciona linhas 
with open('manipulação de arquivos/teste.txt','w', encoding ='utf-8') as arquivo:

    arquivo.write("Primeira Linha\n")
    arquivo.write("Segunda Linha\n")



#Adiciona linhas no .txt depois
with open('manipulação de arquivos/teste.txt','a', encoding='utf-8') as arquivo:

    arquivo.write("Terceira Linha\n")
    arquivo.write("Quarta Linha\n")



#Lê o arquivo inteiro em str
with open('manipulação de arquivos/teste.txt','r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    
    
#testando