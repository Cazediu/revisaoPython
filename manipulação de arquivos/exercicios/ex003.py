with open('manipulação de arquivos/exercicios/diario.txt','r', encoding='utf-8') as arquivo:

    qtnd_linhas = 0
    qtnd_palavras = 0
    
    for linha in arquivo:
        qtnd_linhas += 1
        palavras = linha.split() 
        qtnd_palavras += len(palavras)
    
print(f"O arquivo tem {qtnd_linhas} linhas")
print(f"O arquivo tem {qtnd_palavras} palavras")
