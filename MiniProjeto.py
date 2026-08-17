import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

#Carregando os dados
dados = pd.read_csv('Base_Varejo.csv', sep=";")

#Quantidade de registros e tipos de dados
print(f"Quantidade de linhas: {dados.shape}")

print("Quantidade de Valores Nulos:", dados.isnull().sum())

print("Quantidade de Registros Duplicados:", dados.duplicated().sum())

#Remover duplicatas
dados = dados.drop_duplicates()
print("Quantidade de Registros após remover duplicatas:", dados.shape)

#Converter data para Datetime
dados['DATA'] = pd.to_datetime(dados['DATA'], errors='coerce')

#Remover colunas vazias
dados = dados.dropna(axis=1, how='all')

#Dados da coluna de Filhos
contagem = dados['CL_FHL'].count()
media = dados['CL_FHL'].mean()
mediana = dados['CL_FHL'].median()
desvio_padrao = dados['CL_FHL'].std()
moda = dados['CL_FHL'].mode()[0]
minimo = dados['CL_FHL'].min()
maximo = dados['CL_FHL'].max()

print(f"Total de Filhos: {contagem}")
print(f"Média de Filhos: {media:.2f}")
print(f"Mediana de Filhos: {mediana}")
print(f"Desvio Padrão de Filhos: {desvio_padrao:.2f}")
print(f"Moda de Filhos: {moda}")
print(f"Mínimo de Filhos: {minimo}")
print(f"Máximo de Filhos: {maximo}")

#Quartis
q25 = dados['CL_FHL'].quantile(0.25)
q50 = dados['CL_FHL'].quantile(0.50)  # Equivalente à mediana
q75 = dados['CL_FHL'].quantile(0.75)

print(f"1º Quartil (25%): {q25}")
print(f"2º Quartil (50% - Mediana): {q50}")
print(f"3º Quartil (75%): {q75}")


#Vendas por gênero
vendas_por_genero = dados.groupby('CL_GENERO')['CO_ID'].count()
print("\n--- Compras por Gênero ---")
print(vendas_por_genero)

#Categorias mais vendidas
vendas_por_categoria = dados.groupby('PR_CAT')['CO_ID'].count().sort_values(ascending=False)
print("\n--- Top Categorias Mais Vendidas ---")
print(vendas_por_categoria.head(5))

#Separando vendas por gênero e top 5 categorias mais vendidas

vendas_por_genero = dados['CL_GENERO'].value_counts()
top_categorias = dados['PR_CAT'].value_counts().head(5)

#Fazendo a estrutura do gráfico
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

#Desenhando o gráfico de barras
vendas_por_genero.plot(kind='bar', ax=ax1, color='blue', edgecolor='black')
ax1.set_title('Volume de Compras por Gênero')
ax1.set_xlabel('Gênero')
ax1.set_ylabel('Quantidade')
ax1.tick_params(axis='x', rotation=0)

#Gráfico por top 5 categorias
top_categorias.plot(kind='barh', ax=ax2, color='green', edgecolor='black')
ax2.set_title('Top 5 Categorias Mais Vendidas')
ax2.set_xlabel('Quantidade de Vendas')
ax2.set_ylabel('Categoria')
ax2.invert_yaxis()

plt.show()