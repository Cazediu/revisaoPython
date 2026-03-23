import csv
       
dados = [
    ['nome','nota','turma'],
    ['ana',8.5,'1E'],
    ['beto',7,'1E'],
    ['carla',9.3,'1E'],
]


with open('arquivos csv/alunos.csv','w',
          encoding='utf-8',
          newline='') as arquivo:

    escritor = csv.writer(arquivo)
    
    for linha in dados:
        escritor.writerow(linha)
    
    
    
with open('arquivos csv/alunos.csv','r',
          encoding='utf-8') as arquivo:
    
    leitor = csv.reader(arquivo)
    
    for linha in leitor:
        print(linha)
        
        
    