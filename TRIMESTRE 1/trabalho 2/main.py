# Projeto Prático - Análise de Dados de Felicidade Mundial
# Autor: Trabalho em dupla (exemplo)
# Objetivo: Explorar o índice de felicidade por país usando Pandas, NumPy e Matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Parte 1 - Carregamento e Exploração Inicial
# -----------------------------
df = pd.read_csv("trabalho 2\world_happiness_2026 (3).csv")

print("Primeiras linhas:")
print(df.head())

print("\nShape (linhas, colunas):", df.shape)
print("\nTipos de dados:")
print(df.dtypes)
print("\nResumo info():")
print(df.info())
print("\nEstatísticas descritivas:")
print(df.describe())

# -----------------------------
# Parte 2 - Limpeza e Preparação
# -----------------------------
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# Garantir que colunas numéricas estejam corretas
df["score"] = df["score"].astype(float)

# Remover duplicatas (se houver)
df = df.drop_duplicates()

print("\nShape após limpeza:", df.shape)

# -----------------------------
# Parte 3 - Análises com Pandas e NumPy
# -----------------------------

# a) Filtros condicionais

# Filtro 1: Países com score maior que a média e GDP menor que a média
media_score = df["score"].mean()
media_gdp = df["gdp_per_capita"].mean()
filtro1 = df[(df["score"] > media_score) & (df["gdp_per_capita"] < media_gdp)]
print("\nFiltro 1: Países com score > média e GDP < média")
print(filtro1[["country","score","gdp_per_capita"]])

print("\nMédia do score:", media_score)
print("Média do GDP:", media_gdp)

# Filtro 2: Países da América Latina com índice de felicidade maior que a Grécia
score_grecia = df[df["country"] == "Greece"]["score"].values[0]
filtro2 = df[(df["region"].str.contains("Latin America")) & (df["score"] > score_grecia)]
print("\nFiltro 2: Países da América Latina com score > Grécia")
print(filtro2[["country","region","score"]])

print("\nScore da Grécia:", score_grecia)
print("OBS: A Grécia é o pais da europa com menor score do arquivo ")

# Filtro 3: Países com menor liberdade e que tenham score acima da média
media_liberdade = df["freedom"].mean()
filtro3 = df[(df["freedom"] < media_liberdade) & (df["score"] > media_score)]
print("\nFiltro 3: Países com liberdade < média e score > média")
print(filtro3[["country","score","freedom"]])

print("\nmedia_liberdade:", media_liberdade)
print("media_score:", media_score)

# b) Ordenação
print("\nTop 10 países mais felizes:")
print(df.sort_values("score", ascending=False).head(10)[["country","score"]])

print("\nBottom 10 países menos felizes:")
print(df.sort_values("score", ascending=True).head(10)[["country","score"]])

# c) Agrupamento e agregação
print("\nMédia de felicidade por região:")
print(df.groupby("region")["score"].mean())

print("\nMédia e máximo de GDP por região:")
print(df.groupby("region")["gdp_per_capita"].agg(["mean","max"]))

# d) Operações com NumPy
print("\nDesvio padrão do score:", np.std(df["score"]))

print("\nCorrelação entre GDP e Score:")
print(np.corrcoef(df["gdp_per_capita"], df["score"]))

# Classificação em terços do índice de felicidade (score)
df["indice_classificacao"] = pd.qcut(df["score"], 
                                     q=3, 
                                     labels=["indice baixo", "indice medio", "indice alto"])

print("\nColuna 'indice_classificacao' criada:")
print(df[["country","score","indice_classificacao"]].head(15))


# -----------------------------
# Parte 4 - Visualizações
# -----------------------------

#10 países mais felizes do mundo
plt.figure(figsize=(8,5))
sns.barplot(x="country", y="score", data=df.head(10))
plt.xticks(rotation=45)
plt.title("Top 10 Países mais Felizes")
plt.xlabel("País")
plt.ylabel("Score")
plt.savefig("top10.png")
plt.tight_layout()
plt.show()

#Distribuição de países por score
plt.figure(figsize=(8,5))
plt.hist(df["score"], bins=20, color="skyblue")
plt.title("Distribuição do Score de Felicidade")
plt.xlabel("Score")
plt.ylabel("Frequência")
plt.savefig("hist_score.png")
plt.show()

#Relação entre GPD e o score
plt.figure(figsize=(8,5))
plt.scatter(df["gdp_per_capita"], df["score"], color="green")
plt.title("Relação entre GDP per capita e Score")
plt.xlabel("GDP per capita")
plt.ylabel("Score")
plt.savefig("relacao_gdp_score.png")
plt.show()


#Boxplot por região
plt.figure(figsize=(8,5))
sns.boxplot(x="region", y="score", data=df)
plt.xticks(rotation=90)
plt.title("Distribuição do Score por Região")
plt.savefig("boxplot_region.png")
plt.show()

# -----------------------------
# Parte 4 - Heatmap de Correlação
# -----------------------------

# Seleciona apenas colunas numéricas do DataFrame
df_numerico = df.select_dtypes(include=["float64","int64"])

# Calcula a matriz de correlação
corr = df_numerico.corr()

# Cria o mapa de calor com Seaborn
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)

# Comentários:
# - Cada célula mostra o coeficiente de correlação entre duas variáveis numéricas.
# - Azul indica correlação positiva, vermelho indica negativa.
# - Isso ajuda a identificar relações fortes, como GDP per capita vs score.
plt.title("Mapa de Calor das Correlações")
plt.savefig("heatmap_corr.png")
plt.show()



# -----------------------------
# Parte 5 - Descobertas
# -----------------------------
print("\nDescobertas:")
print("1. Países nórdicos lideram consistentemente o ranking de felicidade.")
print("2. Há forte correlação positiva entre GDP per capita e score, mostrando a grande dependência da\n felicidade em relação o capital financeiro")
print("3. Algumas regiões da América Latina aparecem com scores relativamente altos apesar de GDP menor.")
print("4. Falando de geopolítica, países que foram colonizados consequentemente tem um score menor. Já\n páises que foram colonizadores apresentam níveis muito maiores ")
print("5. A classificação em terços ajuda a visualizar de forma mais prática quais países estão em índice alto, médio ou baixo.")
