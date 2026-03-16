dados = {
    'nome': 'Cazé',
    'telefone':999999999,
    'email': 'cazeportela@gmail.com',
    'cidade': 'Rio Pomba',
}

dados['instagram'] = '@cazediu'
del dados['telefone']
print(dados.items())

if 'email' in dados:
    print("existe email")
else:
    print("Não existe email")