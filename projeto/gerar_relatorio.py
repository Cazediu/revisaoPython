# -------------------------------
# Função para ler e limpar os dados do CSV
# -------------------------------
def ler_csv(arquivo):
    dados = []
    with open(arquivo, encoding="latin-1") as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            linha_limpa = {chave: (valor.strip() if valor.strip() != "" else "0") for chave, valor in linha.items()}
            dados.append(linha_limpa)
    return dados

# -------------------------------
# Estatísticas auxiliares
# -------------------------------
def media_campo(dados, campo):
    valores = [int(musica[campo]) for musica in dados if musica[campo].isdigit()]
    return sum(valores) / len(valores)

def frequencia(dados, campo):
    contagem = {}
    for musica in dados:
        valor = musica[campo]
        contagem[valor] = contagem.get(valor, 0) + 1
    mais = max(contagem, key=contagem.get)
    menos = min(contagem, key=contagem.get)
    return mais, contagem[mais], menos, contagem[menos]

def contar_registros(dados):
    return len(dados)

# -------------------------------
# Filtros específicos
# -------------------------------
def filtro_eletronicas_pop_acima_media(dados, media_pop):
    resultado = [m for m in dados if any(g in m["top genre"].lower() for g in ["electro","edm","house"])]
    resultado = [m for m in resultado if m["pop"].isdigit() and int(m["pop"]) > media_pop]
    return resultado

def filtro_artistas_menos_pop_antes_2016(dados):
    resultado = [m for m in dados if m["year"].isdigit() and int(m["year"]) < 2016]
    resultado.sort(key=lambda x: int(x["pop"]) if x["pop"].isdigit() else 0)
    return resultado

def filtro_artistas_mais_pop_depois_2016(dados):
    resultado = [m for m in dados if m["year"].isdigit() and int(m["year"]) >= 2016]
    resultado.sort(key=lambda x: int(x["pop"]) if x["pop"].isdigit() else 0, reverse=True)
    return resultado

# -------------------------------
# Relatório automático
# -------------------------------
def gerar_relatorio_automatico(dados, arquivo="relatorio_projeto.txt"):
    nome_dataset = "top10s.csv"
    descricao = "Dataset com músicas populares do Spotify entre 2010 e 2019, incluindo artista, gênero, BPM e popularidade."

    total_registros = contar_registros(dados)
    total_colunas = len(dados[0]) if dados else 0

    media_bpm = media_campo(dados, "bpm")
    media_pop = media_campo(dados, "pop")
    artista_mais, qmais, artista_menos, qmenos = frequencia(dados, "artist")
    genero_mais, qgmais, genero_menos, qgmenos = frequencia(dados, "top genre")

    # Filtros
    eletronicas = filtro_eletronicas_pop_acima_media(dados, media_pop)
    menos_pop_antes2016 = filtro_artistas_menos_pop_antes_2016(dados)
    mais_pop_depois2016 = filtro_artistas_mais_pop_depois_2016(dados)

    conteudo = (
        "Relatório do Projeto - Análise de Músicas Spotify\n\n"
        
        f"Nome do dataset: {nome_dataset}\n"
        f"Descrição: {descricao}\n\n"
        
        
        f"Quantidade total de registros: {total_registros}\n"
        f"Quantidade de colunas: {total_colunas}\n\n"
        
        "Estatísticas gerais:\n"
        f"- Artista mais frequente: {artista_mais} ({qmais} registros)\n"
        f"- Artista menos frequente: {artista_menos} ({qmenos} registros)\n"
        f"- Gênero mais frequente: {genero_mais} ({qgmais} registros)\n"
        f"- Gênero menos frequente: {genero_menos} ({qgmenos} registros)\n"
        f"- Média de BPM: {media_bpm:.2f}\n"
        f"- Média de Popularidade: {media_pop:.2f}\n"
        f"- Contagem de registros válidos: {total_registros}\n\n"
        
        "Filtros aplicados:\n\n"
        
        f"1. Músicas eletrônicas com popularidade acima da média:\n"
        f"   Quantidade: {len(eletronicas)}\n"
        f"   Exemplos: {[m['title'] for m in eletronicas[:10]]}\n\n"
        
        f"2. Artistas com menos popularidade antes de 2016:\n"
        f"   Quantidade: {len(menos_pop_antes2016)}\n"
        f"   Exemplos: {[m['artist'] for m in menos_pop_antes2016[:10]]}\n\n"
        
        f"3. Artistas com mais popularidade depois de 2016:\n"
        f"   Quantidade: {len(mais_pop_depois2016)}\n"
        f"   Exemplos: {[m['artist'] for m in mais_pop_depois2016[:10]]}\n\n"
        
        "Conclusões:\n"
        "- O gênero 'dance pop' domina o dataset, refletindo a tendência da década.\n"
        "- A popularidade média mostra que a maioria das músicas analisadas foi bem recebida.\n"
        "- Apesar do grande número de artistas que foram ouvidos, apenas alguns tem mais de 2 registros.\n"
    )

    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"Relatório automático gerado em {arquivo}")

# -------------------------------
# Execução principal
# -------------------------------
if __name__ == "__main__":
    dados = ler_csv("top10s.csv")
    gerar_relatorio_automatico(dados)
    menu(dados)# gera o relatório automaticamente
