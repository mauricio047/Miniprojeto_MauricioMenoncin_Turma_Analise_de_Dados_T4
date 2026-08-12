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
