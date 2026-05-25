def limpar_reprovados(lista_notas):
    
    lista_aprovados = []
    
    for i in range (len(lista_notas)):
        if lista_notas[i] >= 6:
            lista_aprovados.append(lista_notas[i])
    
    print(lista_aprovados)
        
        
lista_notas = [5.0, 7.0, 4.5, 9.0, 6.0, 3.0, 8.5]       
limpar_reprovados(lista_notas)