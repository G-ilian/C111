# Exercicio 03
import pandas as pd
import numpy as np

dfPaises=pd.read_csv('paises.csv',delimiter=';')

# Nome e região do planeta que possui a maior população
pop=dfPaises['Population']
idx_max=pop.idxmax()

regiao=dfPaises['Region'].values[idx_max]
pais=dfPaises['Country'].values[idx_max]
max_pop=dfPaises['Population'].max()

print('\n ---- NOME,REGIÃO E POPULAÇÃO DA MAIOR POP DA TERRA')
print(f'REGION: {regiao} -- COUNTRY: {pais} -- POPULATION: {max_pop}')