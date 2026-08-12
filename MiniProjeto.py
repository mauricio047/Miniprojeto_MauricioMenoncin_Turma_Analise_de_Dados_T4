import pandas as pd
import datetime as dt

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

