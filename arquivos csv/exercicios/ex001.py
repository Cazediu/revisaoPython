import csv

dados = [
    ['nome','nota1','nota2']
]


for linha in range(3):
    
    dadosAlunos = []
    
    nome = input("Qual o nome do aluno? ")
    nota1 = input("Qual a nota 1 do aluno? ")
    nota2 = input("Qual o nota 2 do aluno? ")
        
    
    dadosAlunos.append(nome)
    dadosAlunos.append(nota1)
    dadosAlunos.append(nota2)
        
    dados.append(dadosAlunos)
    
with open('arquivos csv/exercicios/alunos.csv','w',
          encoding='utf-8',
          newline='') as arquivo:

    escritor = csv.writer(arquivo)
    
    for linha in dados:
        escritor.writerow(linha)