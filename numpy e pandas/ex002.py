import pandas as pd

df = pd.read_csv('jogos.csv')

#df['genero'].value_counts()            # Minha previsão: Quantos jogos tem por cada genero
#df['nota'].max()                       # Minha previsão: A nota máxima que um jogo tem 
#df['preco'].min()                      # Minha previsão: Preço mínimo de um jogo
#df.loc[5, 'jogo']                      # Minha previsão: Nome do jogo na linha 5
#df.iloc[0:3, 1:3]                       # Minha previsão: Genrero e nota dos 3 primeiros jogos
#df[['jogo', 'ano']].tail(3)            # Minha previsão: Nome e data dos últimos jogos
#df.describe().loc['mean']              # Minha previsão: A média de cada coluna com números inteiros
