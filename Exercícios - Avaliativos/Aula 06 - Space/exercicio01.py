import numpy as np

#Importando o dataset com as missões espaciais
spaceDS=np.loadtxt("space.csv",delimiter=';',dtype=str,encoding='utf-8')

# Variaveis de controle do sistema
num_missoes=np.max(spaceDS[1:,0].astype('int32'))
status_missoes=spaceDS[1:,7].copy()
status=np.char.endswith(status_missoes,"Success")
num_missoes_sucesso=np.sum(status)

# Mostrando o pedido dos exercícios
print('+++++++++++++++++++++++++++++++++++ \n')
print(f'Número de missões: {num_missoes}')
print(f'Missões que obtiveram sucesso: {num_missoes_sucesso}')
porcentagem_sucesso=(100*num_missoes_sucesso)/num_missoes
print(f'Porcentagem de missões que obtiveram sucesso {porcentagem_sucesso.round(2)} %')

