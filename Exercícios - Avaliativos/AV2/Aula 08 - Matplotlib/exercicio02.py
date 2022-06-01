# Imports 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Abrindo dataframe
dfPaises=pd.read_csv('paises.csv',delimiter=';')

# Coletando apenas os países da América do Norte
dfAmericaNorte=dfPaises.loc[dfPaises['Region'].str.contains('NORTHERN AMERICA')]

x=np.array([1,2,3,4,5])
y=dfAmericaNorte['Deathrate']
y2=dfAmericaNorte['Birthrate']

plt.plot(x,y,'r-',x,y2,'b--')
plt.show()