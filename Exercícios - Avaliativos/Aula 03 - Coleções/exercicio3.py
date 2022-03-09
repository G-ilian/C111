#### Exercício 2 - Alunos ######

nomeAluno=input("Nome: ")
mediaAluno=int(input("Média: "))

dados={'nome':nomeAluno,'media':mediaAluno}

if(mediaAluno>=60):
    dados['Situacao Final']='AP'
else:
    dados['Situacao Final']='AP'

for k,v in dados.items():
    print(f'{k} é {v}')