import numpy as np
#Importando o dataset com as missões espaciais
spaceDS=np.loadtxt("space.csv",delimiter=';',dtype=str,encoding='utf-8')


def conta_quantidade(empresas):
    count=0
    for empresa in empresas:
        aux=np.char.find(spaceDS[1:,1],empresa)
        num_missoes=np.sum(aux)+spaceDS[1:,1].size
        print(f'Company: {empresa} \nTotal of missions:{num_missoes} ')
    


companhias=np.unique(spaceDS[1:,1])

conta_quantidade(companhias)

