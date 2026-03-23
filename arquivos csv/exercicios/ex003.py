import csv 
listaMedia = []

with open('arquivos csv/exercicios/notas.csv','r',
          encoding='utf-8') as arquivo:
    
    leitor = csv.reader(arquivo)
    cabecalho = next(leitor)
    
    dados_com_media = [cabecalho]
    
    for linha in leitor:
        
        media = (float(linha[1]) + float(linha[2])) / 2
        cabecalho.append('media')
        linha.append(media)
        dados_com_media.append(linha)
        


with open('arquivos csv/exercicios/notas_com_media.csv','w',
          encoding='utf-8', newline='') as arquivo_saida:
        
    escritor = csv.writer(arquivo_saida)
    escritor.writerows(dados_com_media)