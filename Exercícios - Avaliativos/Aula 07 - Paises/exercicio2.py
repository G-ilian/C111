# Exercicio 02
import pandas as pd
import numpy as np


dfPaises=pd.read_csv('paises.csv',delimiter=';')

# Média de alfabetização do planeta

alfabetizacao=dfPaises[['Literacy (%)']]
print('---- Média de alfabetização do mundo ----')
print(alfabetizacao.mean(axis=0))