from BancoArquivos.Módulos.modulosBanco import *
from BancoArquivos.Listas.listas import *

# Início


saldototal = randint(100, 13000)
saldototal_info.append(saldototal)

clean()

print('DIGITE ENTER PARA ENTRAR...')

while True:

    inicio = input('')

    if inicio == '':
        music('Sons/gta.mp3')
        clean()
        break

    elif inicio.strip().lower() == 'dev':
        os.system('start Dev/dev.py')

    else:
        print('')

music('Sons/bemvindo.mp3')
sleep(4)

blue('BANCO VIRTUAL DA SAINT GERMAIN')
lin2_30()

while True:

    usuario = input('Digite seu Usuário: ').lower().strip()

    if usuario not in usuarios[0]:
        usuarios[0].append(usuario)

    else:
        print('', end='')

    while True:

        senha = input('Digite sua Senha: ').strip()

        if senha == '4120' and usuario != 'eduardo':
            clean()
            red('SENHA JÁ UTILIZADA!')
            lin_0()

        elif senha == '4120' and usuario == 'eduardo':
            clean()
            break

        if len(senha) != 4:
            clean()
            lin_0()
            red('DIGITE APENAS 4 NÚMEROS!')
            lin_0()

        else:
            break

    if senha not in usuarios[1]:
        usuarios[1].append(senha)


    else:
        print('', end='')

    clean()
    music('Sons/gta.mp3')

    if usuario != 'eduardo' and senha != '4120' or usuario == 'eduardo' and senha != '4120':
        lin_0()
        lin_0()
        blue('< BEM VINDO AO BANCO VIRTUAL DA SAINT GERMAIN >')
        break

    else:
        clean()
        music(f'{random.choice(narradores)}')
        blue('BEM\nVINDO\nDE\nVOLTA\nEDUARDO')
        break

################################################################################################
# Opções

while True:

    sleep(2)
    clean()
    lin_0()
    lin_0()
    print('*=' * 30)

    print('O Que Você Deseja Fazer?')
    print('.' * 30)

    print('Digite [0] Para Ver Seu', end=' ')
    green('SALDO TOTAL')

    print('Digite [1] Para Fazer Uma', end=' ')
    green('TRANSFERÊNCIA')

    print('Digite [2] Para Fazer Um', end=' ')
    green('SAQUE')

    print('Digite [3] Para Fazer Um', end=' ')
    green('DEPÓSITO')

    print('Digite [4] Para', end=' ')
    red('SAIR')

    lin2_30()
    print('Fale Conosco! 9999123999')
    lin2_30()
    white('1.0')
    lin_0()

    resposta = input('')

    ####################################################

    # SaldoTotal

    if resposta == '0':

        while True:

            music('Sons/gta.mp3')
            clean()

            print(f'\033[97;1mSALDO TOTAL\033[m: \033[32;1mR${saldototal:.2f}\033[m')

            print(f'\033[97;1m{usuario.capitalize().strip().title()}\033[m', end='  ')

            print(f'\033[97;1mSenha: {senha}\033[m', end='  ')

            lin_0()
            lin2_30()

            red('DIGITE ENTER PARA SAIR...')

            r_0 = input('')

            r_0.strip().title()

            if r_0 == '':
                music('Sons/gtaero.mp3')
                clean()
                break

            else:
                lin_0()


    #########################################
    # Trasferência

    elif resposta == '1':

        music('Sons/gta.mp3')

        clean()

        nomet = input(
            'Digite o \033[34;1mNOME COMPLETO\033[m da Pessoa Em Que Deseja Fazer a \033[34;1mTRANSFERÊNCIA\033[m [EXP: matheus suáres dos santos]: ').lower().strip()

        if nomet != 'eduardo henrique markevicz' or 'eduardohenriquemarkevicz' == True:
            lin_0()
            clean()


        else:
            clean()
            print(
                f'O \033[32;1mEduardo\033[m já é Nosso Cliente, Por Conta Disso Você Recebe \033[32;1m5%\033[m de \033[32;1mCashback\033[m!')

        while True:

            lin_0()
            numconta = input('Qual é o NÚMERO da CONTA? [4 NÚMEROS]: ')
            clean()
            lin_0()

            if len(numconta) != 4:
                red('DÍGITE APENAS 4 NÚMEROS!')


            else:
                clean()
                break


        while True:

            green(f'SALDO DISPONÍVEL: R${saldototal:,}')
            lin_0()

            dint = int(input('Valor Da TRANSFERÊNCIA: R$'))

            if dint > saldototal:
                clean()
                red('VOCÊ NÃO PODE DEPOSITAR ESTE VALOR!')

            else:
                break

        lin2_30()
        while True:

            print(f'Você Deseja Fazer a TRANSFERÊNCIA no Valor de \033[1;32mR${dint:,}\033[m')
            rt1 = (str(input(
                f'Para a Conta de \033[1;33m{nomet.strip().capitalize().title()}?\033[m [S]/[N]: '))).strip().lower()

            if rt1 == 's':

                saldototal -= dint

                music('Sons/gta.mp3')

                lin2_30()

                break

            elif rt1 == 'n':
                music('Sons/gtaero.mp3')
                clean()
                lin_0()
                red('TRANSFERÊNCIA CANCELADA!')
                sleep(2)

                break


            else:
                clean()

        while True:

            if rt1 == 'n':
                break

            sleep(3)

            print('\033[1;32mTRASFERÊNCIA REALIZADA COM SUCESSO!\033[m')

            music('Sons/transferencia.mp3')

            lin_0()

            blue(f'VALOR DA TRASFERÊNCIA: \033[32;1mR${dint:2,}\033[m')
            blue(f'OPERAÇÃO NÚMERO: \033[97;1m{randint(5000, 16000)}\033[m')
            blue(
                f'TRASFERÊNCIA DE \033[97;1m{usuario.upper()}\033[m \033[34mPARA\033[m \033[97;1m{nomet.upper()}\033[m')

            lin_0()

            white(f'{datetime.datetime.now()}')

            lin_0()

            cashback = dint * 5 / 100

            if nomet == 'eduardo henrique markevicz' or 'eduardohenriquemarkevicz' == True and numconta == '4120' == True:
                green(f'Você Recebeu R${cashback} de Cashback!')
                saldototal += cashback

            else:
                lin_0()

            lin_0()
            red('DIGITE ENTER PARA SAIR...')
            r_t = input('')

            if r_t == '':
                music('Sons/gtaero.mp3')
                clean()
                break

            else:
                print('')

            saldototal = saldototal - dint


    ##########################################################
    # Saque

    elif resposta == '2':

        while True:

            clean()
            green(f'SALDO DISPONÍVEL: R${saldototal:,}')
            lin_0()

            dinsaque = int(input('Digite a Quantidade em que Deseja Sacar: R$'))

            if dinsaque > saldototal:
                lin_0()
                red('VOCê NÃO PODE SACAR ESSA QUANTIA EM DINHEIRO!')

            else:
                break

        while True:

            if dinsaque < saldototal or dinsaque == saldototal:

                music('Sons/impressora.mp3')
                print('SACANDO DINHEIRO...')
                sleep(3)

                saldototal -= dinsaque

                print('AGUARDE...')
                sleep(4)

                print('#' * 30)
                lin_0()

                white(datetime.datetime.now())

                saques[1].append(datetime.datetime.now())

                lin_0()
                green('DINHEIRO SACADO COM SUCESSO!')
                sleep(1)

                lin_0()
                green(f'R${dinsaque}')
                sleep(3)
                lin_0()

                red('DIGITE ENTER PARA SAIR...')
                r_s = input('')

                if r_s == '':
                    music('Sons/gtaero.mp3')
                    break

                else:
                    lin_0()

                saques[0].append(dinsaque)


    #####################
    # Depósito

    elif resposta == '3':

        music('Sons/gta.mp3')
        clean()

        while True:

            deposito = int(
                input('Digite a Quantidade em que Deseja Depositar \033[33;1m[ LIMITE DE 10,000R$ ]\033[m: R$'))

            if deposito > 10000:
                clean()
                lin_0()
                red('VOCÊ NÃO PODE DEPOSITAR ESTE VALOR!')
                lin_0()

            else:
                clean()
                break

        while True:

            clean()
            music('Sons/contando.mp3')

            print('CONTANDO DINHEIRO...')
            sleep(3)

            print('AGUARDE...')
            sleep(4)

            print('#' * 30)

            green('DINHEIRO DEPOSITADO COM SUCESSO!')
            lin_0()

            green(f'R${deposito}')
            lin_0()

            white(datetime.datetime.now())
            lin_0()

            saldototal += deposito

            red('DIGITE ENTER PARA SAIR...')

            respdepo = input('')

            if respdepo == '':
                clean()
                music('Sons/gtaero.mp3')
                break

            else:
                lin_0()


    ####################################################################

    elif resposta == '4':

        music('Sons/gta.mp3')
        sleep(1)
        print('#' * 40)

        if usuario == 'eduardo':
            music('Sons/valeu.mp3')

        print('FiNALIZANDO...')
        sleep(2)
        clean()
        sleep(4)

        break

    else:
        lin_0()
