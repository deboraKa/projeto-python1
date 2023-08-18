import numpy as np

#Criando minha lista

reserva = []
posi = np.arange(40).reshape(8,5) # 40 lugares, para uma matriz 8x5
posi = np.where(posi == posi[0][0],'M',posi) # Posição do motorista
posi[0][1:5] = 'C'
posi[:, 2] = 'C' # Posição corredor

while True:
    print("=" * 30)
    print('Seja bem vindo a Poccobus!')
    print("=" * 30)
    print('\n[1] - Reserva de Assentos')
    print('\n[2] - Encerrar')
    print("=" * 30)
    opcao = str(input('\n Qual operação deseja realizar? '))
    try:
#Inserindo exceções e tratamento de erro
        if int(opcao) == 0 or int(opcao) > 2:
            print('valor inválido, tente novamente!')

    except ValueError:

        print('Digite um valor válido')
#Reserva de poltronas
    if opcao == '1':
        print('=' * 45)
        print('SISTEMA DE RESERVA POCCOBUS'.center(45))
        print('=' * 45)
        print("R = Reservado")
        print("C = Corredor")
        print('M =  Motorista')
        print()
        while opcao != 'N':
            print(posi)
            x = str(input('Escolha uma poltrona: '))
            while x in reserva or x not in posi or x == 'C' or x == 'M':
                x = str(input(' Digite um assento válido!: '))
            else:
                reserva.append(x)
            for x in reserva:
                posi = np.where(posi == x, 'R', posi)
            print(f'Você reservou a Poltrona {reserva} !')

            r = input('Gostaria de continuar? [S/N] ').upper().strip()
            if r == 'S':
                print('=' * 45)
                print('SISTEMA DE RESERVA POCCOBUS'.center(45))
                print('=' * 45)
                print("R = Reservado")
                print("C = Corredor")
                print('M =  Motorista')
                print()
                for a in enumerate(reserva): #puxa a matriz com as reservas realizadas.
                    print(f'Reservado {a}')
                print()
            elif r == 'N':
                print('Relação Final dos Assentos:')
                print("=" * 30)
                print('Poccobus')
                print("=" * 30)
                for a in enumerate(reserva):
                    print(f'Reservado {a}')
                print()
                print("=" * 30)
                print('RESERVA EFETUADA COM SUCESSO!')
                print("=" * 30)
                break
            else:
                print('Opção Inválida! Tente novamente.')

    elif opcao == '2':
        print('=' * 30)

        print('ENCERRANDO')

        print('=' * 30)
        print('Seu arquivo foi gerado com sucesso!')
        with open('relatorio_poccobus.txt', 'w') as arquivo:
            arquivo.write('Reservas efetuadas\n')
            for num in reserva:
                arquivo.write(str(num) + '-')
            arquivo.write('\nDisponiveis para reservar \n')
            for num2 in posi.ravel().tolist():
                if num2 != 'C' and num2 != 'M' and num2 != 'R':
                    arquivo.write(str(num2) + '-')















