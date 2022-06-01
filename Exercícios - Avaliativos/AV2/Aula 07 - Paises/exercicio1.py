# Exercicio 01 
import pandas as pd

dfPaises=pd.read_csv('paises.csv',delimiter=';')

# a - Quais os paises são da oceania
listaOceania=dfPaises.loc[dfPaises['Region'].str.contains('OCEANIA')]
paisesOceania=listaOceania['Country'].values[:]
print('---- Países da Oceania ---- \n')
for pais in paisesOceania: 
    print (pais)

# b - Número de países da oceania
print('\n---- Número de países da oceania ---- ')
print(len(paisesOceania))





