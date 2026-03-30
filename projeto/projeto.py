import csv


# Função para ler o CSV
def ler_csv(arquivo):
    dados = []
    # Abrindo o arquivo com encoding latin-1 para evitar erros de acentuação
    with open(arquivo, encoding="latin-1") as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            linha_limpa = {}
            # Limpeza: tira espaços e substitui valores vazios por "0"
            for chave, valor in linha.items():
                if valor.strip() == "":
                    linha_limpa[chave] = "0"
                else:
                    linha_limpa[chave] = valor.strip()
            dados.append(linha_limpa)
    return dados


# Estatísticas básicas
def contar_registros(dados):
    return len(dados)

def media_campo(dados, campo):
    
    valores = []
    
    for musica in dados:
        if musica[campo].isdigit():
            valores.append(int(musica[campo]))
    
    return sum(valores) / len(valores)

def frequencia(dados, campo): #artistas +freq e genero +freq 
    
    contagem = {}
    
    for musica in dados:
        valor = musica[campo]
        
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1
            
    mais_aparece = max(contagem, key=contagem.get)
    menos_aparece = min(contagem, key=contagem.get)
    
    return mais_aparece, contagem[mais_aparece], menos_aparece, contagem[menos_aparece]


# Filtros
def filtro_eletronicas_pop_acima_media(dados, media_pop):
    
    resultado = []
    
    for musica in dados:
        
        genero = musica["top genre"].lower()
        
        if "electro" in genero or "edm" in genero or "house" in genero:
            if musica["pop"].isdigit() and int(musica["pop"]) > media_pop:
                resultado.append(musica)
                
    return resultado

def filtro_artistas_menos_pop_antes_2016(dados):
    
    resultado = []
    
    for a in dados:
        if a["year"].isdigit() and int(a["year"]) < 2016:
            resultado.append(a)
    resultado.sort(key=lambda campo: int(campo["pop"]) if campo["pop"].isdigit() else 0)
    #ordena a lista do menor pro maior, usa função lambda para tribuir os valores de pop e organiza-los

    # pegar apenas artistas únicos
    artistas = [] 
    artistas_vistos = set()
    
    for a in resultado:
        
        artista = a["artist"]
        
        if artista not in a:
            artistas.append(a)
            artistas_vistos.add(artista)
            
    return artistas

def filtro_artistas_mais_pop_depois_2016(dados):
    
    resultado = []
    
    for a in dados:
        if a["year"].isdigit() and int(a["year"]) >= 2016:
            resultado.append(a)
    resultado.sort(key=lambda campo: int(campo["pop"]) if campo["pop"].isdigit() else 0, reverse=True)

    # pegar apenas artistas únicos
    
    artistas = []
    artistas_vistos = set()
    
    for a in resultado:
        
        artista = a["artist"]
        
        if artista not in artistas_vistos:
            artistas.append(a)
            artistas_vistos.add(artista)
            
    return artistas



# Relatório automático
def gerar_relatorio(dados):
    
    #atribuindo valores para o relatorio
    nome_dataset = "top10s.csv"
    descricao = "Dataset com músicas populares do Spotify entre 2010 e 2019."

    total_registros = contar_registros(dados)
    total_colunas = len(dados[0]) if dados else 0

    media_bpm = media_campo(dados, "bpm")
    media_pop = media_campo(dados, "pop")
    artista_mais, qntdmais, artista_menos, qntdmenos = frequencia(dados, "artist")
    genero_mais, qntdgmais, genero_menos, qntdgmenos = frequencia(dados, "top genre")

    eletronicas = filtro_eletronicas_pop_acima_media(dados, media_pop)
    menos_pop_antes2016 = filtro_artistas_menos_pop_antes_2016(dados)
    mais_pop_depois2016 = filtro_artistas_mais_pop_depois_2016(dados)



    #coonteudo em si do relatorio
    conteudo = ""
    conteudo += "Relatório do Projeto - Análise de Músicas Spotify\n\n"
    conteudo += f"Nome do dataset: {nome_dataset}\n"
    conteudo += f"Descrição: {descricao}\n\n"
    conteudo += f"Quantidade total de registros: {total_registros}\n"
    conteudo += f"Quantidade de colunas: {total_colunas}\n\n"

    conteudo += "Estatísticas gerais:\n"
    conteudo += f"- Artista mais frequente: {artista_mais} ({qntdmais})\n"
    conteudo += f"- Artista menos frequente: {artista_menos} ({qntdmenos})\n"
    conteudo += f"- Gênero mais frequente: {genero_mais} ({qntdgmais})\n"
    conteudo += f"- Gênero menos frequente: {genero_menos} ({qntdgmenos})\n"
    conteudo += f"- Média de BPM: {media_bpm:.2f}\n"
    conteudo += f"- Média de Popularidade: {media_pop:.2f}\n"
    conteudo += f"- Contagem de registros válidos: {total_registros}\n\n"

    conteudo += "Filtros aplicados:\n\n"
    
    conteudo += f"1. Músicas eletrônicas com popularidade acima da média:\n"
    conteudo += f"   Quantidade: {len(eletronicas)}\n"
    conteudo += f"   Exemplos: {[m['title'] for m in eletronicas[:10]]}\n\n"
    
    conteudo += f"2. Artistas com menos popularidade antes de 2016:\n"
    conteudo += f"   Quantidade: {len(menos_pop_antes2016)}\n"
    conteudo += f"   Exemplos: {[m['artist'] for m in menos_pop_antes2016[:10]]}\n\n"

    conteudo += f"3. Artistas com mais popularidade depois de 2016:\n"
    conteudo += f"   Quantidade: {len(mais_pop_depois2016)}\n"
    conteudo += f"   Exemplos: {[m['artist'] for m in mais_pop_depois2016[:10]]}\n\n"

    conteudo += "Conclusões:\n"
    conteudo += "- O gênero 'dance pop' domina o dataset com maior número de registros.\n"
    conteudo += "- A popularidade média mostra como apesar de um haver um grande número de musicas.\n"
    conteudo += "- Poucos artistas concentram muitos registros.\n"

    with open("projeto/relatorio_projeto.txt", "w", encoding="utf-8") as f:
        f.write(conteudo)

    print("Relatório automático gerado em relatorio_projeto.txt")


# Menu interativo
def menu(dados):
    while True:
        total = contar_registros(dados)
        print("\n--- MENU ---")
        print(f"Total de registros válidos: {total}")
        print("1 - Artista mais e menos frequente")
        print("2 - Gênero mais e menos frequente")
        print("3 - Média de BPM")
        print("4 - Média de Popularidade")
        print("5 - Filtro: músicas eletrônicas acima da média")
        print("6 - Filtro: artistas menos populares antes de 2016")
        print("7 - Filtro: artistas mais populares depois de 2016")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mais, qmais, menos, qmenos = frequencia(dados, "artist")
            print(f"Mais frequente: {mais} ({qmais}) | Menos frequente: {menos} ({qmenos})")
        elif opcao == "2":
            mais, qmais, menos, qmenos = frequencia(dados, "top genre")
            print(f"Mais frequente: {mais} ({qmais}) | Menos frequente: {menos} ({qmenos})")
        elif opcao == "3":
            print(f"Média de BPM: {media_campo(dados, 'bpm'):.2f}")
        elif opcao == "4":
            print(f"Média de Popularidade: {media_campo(dados, 'pop'):.2f}")
        elif opcao == "5":
            media_pop = media_campo(dados, "pop")
            filtrados = filtro_eletronicas_pop_acima_media(dados, media_pop)
            print(f"{len(filtrados)} músicas encontradas. Exemplos: {[m['title'] for m in filtrados[:10]]}")
        elif opcao == "6":
            filtrados = filtro_artistas_menos_pop_antes_2016(dados)
            print(f"{len(filtrados)} registros. Exemplos: {[m['artist'] for m in filtrados[:10]]}")
        elif opcao == "7":
            filtrados = filtro_artistas_mais_pop_depois_2016(dados)
            print(f"{len(filtrados)} registros. Exemplos: {[m['artist'] for m in filtrados[:10]]}")
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


# Execução principal
if __name__ == "__main__":
    dados = ler_csv("projeto/top10s.csv")
    gerar_relatorio(dados)
    menu(dados)