# Imports 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Abrindo o dataframe
dfSpace=pd.read_csv('space.csv',delimiter=";")

# Obtendo informações acerca do df
qtdEmpUSA=dfSpace['Location'].str.contains('USA').value_counts()[1]
qtdEmpCHN=dfSpace['Location'].str.contains('China').value_counts()[1]

# Plotando
print([qtdEmpUSA,qtdEmpCHN])
labels=['CHN','USA']
plt.bar(labels,[qtdEmpCHN,qtdEmpUSA])
plt.show()