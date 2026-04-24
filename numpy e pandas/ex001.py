import pandas as pd

conteudo = """jogo,genero,nota,preco,ano,plataforma
The Witcher 3,RPG,93,79.90,2015,PC
Celeste,Plataforma,91,36.99,2018,Multi
Hades,Roguelike,93,46.99,2020,Multi
Stardew Valley,Simulação,89,24.99,2016,Multi
Hollow Knight,Metroidvania,90,27.99,2017,Multi
Elden Ring,RPG,96,199.90,2022,Multi
Undertale,RPG,92,21.99,2015,PC
Cuphead,Plataforma,86,37.99,2017,Multi
Dead Cells,Roguelike,89,49.90,2018,Multi
Terraria,Sandbox,83,17.99,2011,PC
Minecraft,Sandbox,93,119.90,2011,Multi
Disco Elysium,RPG,97,69.90,2019,PC
Portal 2,Puzzle,95,19.99,2011,PC
Ori and the Blind Forest,Metroidvania,88,39.99,2015,Multi
Shovel Knight,Plataforma,90,54.90,2014,Multi"""
 
with open('jogos.csv', 'w', encoding='utf-8') as f:
    f.write(conteudo)
 
print("Arquivo jogos.csv criado!")

df = pd.read_csv('jogos.csv')

##LETRA A ------------------

l,c = df.shape

print(f"O dataset possui {l} linhas e {c} colunas.\n\n")

##LETRA B ------------------

print(f"{df.info()}\n\n")

##LETRA C ------------------

print(f"Preço médio: {df['preco'].mean()}")   
print(f"Nota média: {df['nota'].mean()}\n\n")   

##LETRA D ------------------

print(f"Jogos com os maiores preços:\n {df[['jogo', 'preco']].head(3)}\n\n")
 
