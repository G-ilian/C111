#### Exercício 2 - Lojas ######
loja1={'Xiaomi','Asus','Apple'}
loja2={'Motorola','Huawei','Samsung'}

print(f'''A 1ª loja tem {len(loja1)} dispositivo(s) disponíveis\n
Os dispositivos são {loja1}\n''')
print(f'''A 2ª loja tem {len(loja2)} dispositivo(s) disponíveis\n
Os dispositivos são {loja2}''')
cel_iguais=loja1 | loja2
print(f'Modelos de celulares disponíveis em ambas lojas {cel_iguais}')