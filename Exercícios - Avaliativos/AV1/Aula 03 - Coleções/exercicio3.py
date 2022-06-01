#### Exercício 3 - Alunos ######

nomeAluno=input("Nome: ")
mediaAluno=int(input("Média: "))

dados={'nome':nomeAluno,'media':mediaAluno}

if(mediaAluno>=60):
    dados['Situacao Final']='AP'
else:
    dados['Situacao Final']='RP'

print('++++ DADOS DO ALUNO ++++')
for k,v in dados.items():
    print(f'{k} é {v}')