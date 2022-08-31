from BancoArquivos.Listas.listas import *


print('USUÁRIOS:',end=' ')

while True:

    for n in usuarios[0]:
        print(f'{n}'.strip().title().capitalize())
    print('SENHAS:',end=' ')
    for s in usuarios[1]:
        print(f'{s}'.strip().title().capitalize())
        r = input('')

    if r.strip().title() == '':
        break
    else:
        print('')