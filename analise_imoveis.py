import pandas as pd
import matplotlib.pyplot as plt

# Dados simulados diretamente no código (100 imóveis)
data = [
    ["Rio de Janeiro", "Studio", 1, 44, 2891, 718, 3609],
    ["Recife", "Apartamento", 1, 96, 1720, 109, 1829],
    ["Recife", "Studio", 1, 145, 1990, 615, 2605],
    ["São Paulo", "Apartamento", 5, 144, 1486, 251, 1737],
    ["Salvador", "Apartamento", 2, 109, 2345, 203, 2548],
    ["Fortaleza", "Apartamento", 1, 98, 3943, 187, 4130],
    ["Belo Horizonte", "Studio", 1, 121, 1666, 209, 1875],
    ["Belo Horizonte", "Apartamento", 5, 59, 1571, 644, 2215],
    ["Salvador", "Casa", 1, 135, 2052, 450, 2502],
    ["São Paulo", "Casa", 5, 34, 1744, 666, 2410],
    ["Manaus", "Apartamento", 2, 148, 1420, 174, 1594],
    ["São Paulo", "Apartamento", 4, 38, 2794, 246, 3040],
    ["Recife", "Studio", 4, 41, 1937, 654, 2591],
    ["São Paulo", "Casa", 5, 145, 2167, 346, 2513],
    ["Recife", "Apartamento", 5, 116, 2854, 657, 3511],
    ["Curitiba", "Casa", 5, 96, 2650, 648, 3298],
    ["Porto Alegre", "Apartamento", 3, 43, 3860, 471, 4331],
    ["Recife", "Apartamento", 3, 89, 2397, 428, 2825],
    ["Curitiba", "Casa", 3, 101, 3352, 383, 3735],
    ["Recife", "Casa", 2, 74, 3173, 406, 3579],
    ["Recife", "Apartamento", 5, 119, 1740, 768, 2508],
    ["Salvador", "Studio", 1, 45, 2233, 223, 2456],
    ["Recife", "Studio", 4, 147, 1163, 247, 1410],
    ["Recife", "Apartamento", 5, 116, 3615, 408, 4023],
    ["Belo Horizonte", "Casa", 3, 139, 1185, 313, 1498],
    ["Porto Alegre", "Studio", 4, 148, 2310, 333, 2643],
    ["Porto Alegre", "Studio", 3, 45, 1336, 227, 1563],
    ["Curitiba", "Studio", 1, 106, 1444, 720, 2164],
    ["Recife", "Apartamento", 3, 114, 1423, 785, 2208],
    ["Brasília", "Apartamento", 5, 124, 2973, 291, 3264],
    ["Belo Horizonte", "Apartamento", 5, 47, 2284, 740, 3024],
    ["Fortaleza", "Studio", 5, 138, 2572, 330, 2902],
    ["São Paulo", "Casa", 2, 90, 2947, 612, 3559],
    ["Recife", "Studio", 5, 79, 3077, 790, 3867],
    ["Porto Alegre", "Studio", 2, 144, 3193, 678, 3871],
    ["São Paulo", "Apartamento", 1, 134, 3848, 794, 4642],
    ["Salvador", "Studio", 3, 119, 2801, 181, 2982],
    ["Curitiba", "Apartamento", 1, 47, 3700, 274, 3974],
    ["Curitiba", "Studio", 5, 41, 2511, 339, 2850],
    ["Curitiba", "Casa", 2, 78, 2148, 237, 2385],
    ["Porto Alegre", "Apartamento", 4, 120, 2034, 344, 2378],
    ["São Paulo", "Casa", 1, 105, 2053, 770, 2823],
    ["Curitiba", "Apartamento", 1, 55, 1881, 457, 2338],
    ["Recife", "Studio", 2, 40, 1702, 207, 1909],
    ["São Paulo", "Studio", 5, 99, 3016, 321, 3337],
    ["Recife", "Casa", 5, 70, 3497, 162, 3659],
    ["Recife", "Studio", 5, 71, 1554, 562, 2116],
    ["Recife", "Casa", 3, 35, 1235, 504, 1739],
    ["Fortaleza", "Casa", 5, 73, 1960, 745, 2705],
    ["Belo Horizonte", "Casa", 1, 108, 2531, 253, 2784],
    ["Salvador", "Casa", 3, 121, 3664, 408, 4072]
]

colunas = ["Cidade", "Tipo", "Quartos", "Area_m2", "Valor_Aluguel", "Valor_Condominio", "Valor_Total"]
df = pd.DataFrame(data, columns=colunas)

# Gráfico 1: Histograma do Valor Total
plt.figure(figsize=(8, 5))
plt.hist(df["Valor_Total"], bins=15, color="skyblue", edgecolor="black")
plt.title("Distribuição do Valor Total de Aluguel")
plt.xlabel("Valor Total (R$)")
plt.ylabel("Frequência")
plt.grid(True)
plt.tight_layout()
plt.savefig(grafico1_histograma.png)
plt.close()

# Gráfico 2: Boxplot - Valor Total por Número de Quartos
plt.figure(figsize=(8, 5))
df.boxplot(column="Valor_Total", by="Quartos")
plt.title("Valor Total por Número de Quartos")
plt.suptitle("")
plt.xlabel("Número de Quartos")
plt.ylabel("Valor Total (R$)")
plt.tight_layout()
plt.savefig(grafico2_boxplot.png)
plt.close()

# Gráfico 3: Gráfico de barras - Média do Valor Total por Cidade
plt.figure(figsize=(10, 6))
media_cidade = df.groupby("Cidade")["Valor_Total"].mean().sort_values()
media_cidade.plot(kind="bar", color="salmon")
plt.title("Média do Valor Total por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Média do Valor Total (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(grafico3_barras.png)
plt.close()
