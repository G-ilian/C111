#### Exercício 1 - Campeonato Mundial de Futebol ######
times=[]

print('#### BEM VINDO AO CAMPEONATO MUNDIAL DE CLUBES #####')
print('NECESSITAMOS DE ALGUMAS INFORMAÇÕES')
for i in range (5):
    posReal=i+1;
    time=input(f'O {posReal}º colocado do campeonato foi: ')
    times.append(time);

print(f'**** 3º primeiros colocados do campeonato ****\n{times[0:3]}\n')
print(f'**** 2º últimos colocados do campeonato ****\n{times[3:]}\n')

if(times.__contains__('Barcelona')):
    posTimes=int(times.index('Barcelona'))
    posBarca=posTimes+1
    print(f'O Barcelona foi o {(posBarca)}º no campeonato\n')
else:
    print('O Barcelona não participou desse campeonato\n')
times.sort()
print(f'*** Times organizados em ordem alfabética ***\n{times}\n')

