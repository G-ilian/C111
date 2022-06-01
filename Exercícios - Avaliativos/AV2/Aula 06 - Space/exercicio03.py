import numpy as np

#Importando o dataset com as missões espaciais
spaceDS=np.loadtxt("space.csv",delimiter=';',dtype=str,encoding='utf-8')


# Variaveis de controle do sistema
paises_missoes=spaceDS[1:,2]
missoes_EUA=np.char.endswith(paises_missoes,"USA")
num_missoes_USA=np.sum(missoes_EUA)


# Mostrando o pedido dos exercícios
print(f'Foram realizadas {num_missoes_USA} missões pelo Estados Unidos da América')