# Projeto de Revisão de Python - Análise de músicas do Spotify (2010-2019)
# Autor: Carlos
# Objetivo: Ler, tratar e analisar dados de músicas usando apenas recursos nativos do Python.

import csv

# -------------------------------
# Função para ler e limpar os dados do CSV
# -------------------------------
def ler_csv(arquivo):
    dados = []
    # Tente primeiro com 'utf-8', mas se der erro, use 'latin-1'
    with open(arquivo, encoding="latin-1") as f:  # latin-1 aceita acentos comuns
        leitor = csv.DictReader(f)
        for linha in leitor:
            # limpeza simples: remover espaços extras e substituir valores vazios por "0"
            linha_limpa = {chave: (valor.strip() if valor.strip() != "" else "0") for chave, valor in linha.items()}
            dados.append(linha_limpa)
    return dados


# -------------------------------
# Funções de estatísticas
# -------------------------------
def media_campo(dados, campo):
    """Calcula a média de um campo numérico (ex: bpm ou pop)."""
    valores = [int(musica[campo]) for musica in dados if musica[campo].isdigit()]
    return sum(valores) / len(valores)

def artista_mais_frequente(dados):
    """Retorna o artista que mais aparece no dataset."""
    contagem = {}
    for musica in dados:
        artista = musica["artist"]
        contagem[artista] = contagem.get(artista, 0) + 1
    return max(contagem, key=contagem.get)

def genero_mais_frequente(dados):
    """Retorna o gênero musical mais frequente."""
    contagem = {}
    for musica in dados:
        genero = musica["top genre"]
        contagem[genero] = contagem.get(genero, 0) + 1
    return max(contagem, key=contagem.get)

# -------------------------------
# Funções de filtro
# -------------------------------
def filtrar_por_ano(dados, ano):
    """Filtra músicas de um determinado ano."""
    return [musica for musica in dados if musica["year"] == str(ano)]

def filtrar_por_genero(dados, genero):
    """Filtra músicas de um determinado gênero."""
    return [musica for musica in dados if musica["top genre"].lower() == genero.lower()]

# -------------------------------
# Função para salvar relatório
# -------------------------------
def salvar_relatorio(conteudo, arquivo="relatorio_projeto.txt"):
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo)

# -------------------------------
# Menu interativo
# -------------------------------
def menu(dados):
    relatorio = []
    while True:
        print("\n--- MENU ---")
        print("1 - Média de BPM")
        print("2 - Média de Popularidade (pop)")
        print("3 - Artista mais frequente")
        print("4 - Gênero mais frequente")
        print("5 - Filtrar por ano")
        print("6 - Filtrar por gênero")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            resultado = media_campo(dados, "bpm")
            print("Média de BPM:", resultado)
            relatorio.append(f"Média de BPM: {resultado}")
        elif opcao == "2":
            resultado = media_campo(dados, "pop")
            print("Média de Popularidade:", resultado)
            relatorio.append(f"Média de Popularidade: {resultado}")
        elif opcao == "3":
            resultado = artista_mais_frequente(dados)
            print("Artista mais frequente:", resultado)
            relatorio.append(f"Artista mais frequente: {resultado}")
        elif opcao == "4":
            resultado = genero_mais_frequente(dados)
            print("Gênero mais frequente:", resultado)
            relatorio.append(f"Gênero mais frequente: {resultado}")
        elif opcao == "5":
            ano = input("Digite o ano: ")
            filtrados = filtrar_por_ano(dados, ano)
            print(f"Músicas de {ano}: {[m['title'] for m in filtrados]}")
            relatorio.append(f"Músicas de {ano}: {[m['title'] for m in filtrados]}")
        elif opcao == "6":
            genero = input("Digite o gênero: ")
            filtrados = filtrar_por_genero(dados, genero)
            print(f"Músicas do gênero {genero}: {[m['title'] for m in filtrados]}")
            relatorio.append(f"Músicas do gênero {genero}: {[m['title'] for m in filtrados]}")
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

    # Salva relatório final
    salvar_relatorio("\n".join(relatorio))

# -------------------------------
# Execução principal
# -------------------------------
if __name__ == "__main__":
    dados = ler_csv("top10s.csv")
    menu(dados)
