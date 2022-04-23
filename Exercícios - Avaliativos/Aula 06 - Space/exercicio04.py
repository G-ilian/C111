import numpy as np
#Importando o dataset com as missões espaciais
spaceDS=np.loadtxt("space.csv",delimiter=';',dtype=str,encoding='utf-8')

# Variaveis de controle do sistema

missao_spaceX=(spaceDS[1:,(1,6)])
custos=spaceDS[1:,6]
cond=missao_spaceX[0:,0]=="SpaceX"
maior_valor=np.max(custos[cond].astype('float32'))

#Print 
print("++++++++++++++")
print(f'A missão de maior custo da SpaceX foi de {maior_valor} $ milhão de doláres')


