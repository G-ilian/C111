##### Exercício 1 - Array de tamanho 21 com valores linearmente espaçados ######
import numpy as np
val=np.linspace(1,21,num=21)
print(val)

##### Exercício 2 - Concatenação de arrays
import numpy as np
array1=np.arange(0,51,2)
array2=np.arange(100,50,-2)

intervalo_total=np.concatenate((array1,array2))
intervalo_total_ordenado=np.sort(intervalo_total)
print(intervalo_total_ordenado)

##### Exercício 3 - Array ordenado decrescente
intervalo_dec=np.flip(intervalo_total_ordenado)
print("\n ************************************************************\n")
print(intervalo_dec)

##### Exercício 4 - Reshape de matrizes
mat=np.ones((3,4))
mat_reshape=mat.reshape((1,12))
print(mat_reshape)

##### Exercício 5 - Modelamento matrizes
mat2=np.ones((1,7))
linha,coluna=mat2.shape

if ((linha*coluna)%2)==0:
    print("Pode se tornar um vetor com um número par de elementos")
else:
    print("Pode se tornar um vetor com um número impar de elementos")