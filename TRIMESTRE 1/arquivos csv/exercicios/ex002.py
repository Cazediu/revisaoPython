import csv

with open('arquivos csv/exercicios/notas.csv','r',
          encoding='utf-8') as arquivo:
    
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        print(linha['nome'],linha['nota1'],linha['nota2'])
         
        media = (float(linha['nota1']) + float(linha['nota2'])) / 2
        print(f"A média de {linha['nome']} é {media}")
        
        if sum >= 6:
            print(f"{linha['nome']} está APROVADA")
        else:
            print(f"{linha['nome']} está REPROVADO")
        
    
    