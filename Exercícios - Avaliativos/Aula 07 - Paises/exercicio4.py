# Exercicio 04
import pandas as pd
import numpy as np

dfPaises=pd.read_csv('paises.csv',delimiter=';')

# Buscando e salvando em um novo CSV o nome de todos os países que não possuem costa marítima

# 1. Busca
noCoast=dfPaises.loc[dfPaises['Coastline (coast/area ratio)']==0]


# 2. Salvando no novo csv
noCoast['Country'].to_csv('paises_sem_costa.csv',sep=';',header=False)

