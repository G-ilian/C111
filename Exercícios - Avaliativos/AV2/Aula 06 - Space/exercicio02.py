import numpy as np

# Importando o dataset com as missões espaciais
spaceDS=np.loadtxt("space.csv",delimiter=';',dtype=str,encoding='utf-8')

# Variaveis de controle do sistema
num_missoes=np.max(spaceDS[1:,0].astype('int32'))
total_gasto=np.sum(spaceDS[1:,6].astype('float32'))

#Mostrando a média de valores gastos em cada missão
print('+++++++++++++++++++++++++++++++++++ \n')
print(f'Número de missões: {num_missoes}')
print(f'Total gasto com todas as missões: {total_gasto}')
print(f'Média de valor p/ missão : {(total_gasto/num_missoes).round(2)} $ million')