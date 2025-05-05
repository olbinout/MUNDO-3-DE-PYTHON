while True:
    numero = int(input('Digite um número entre 0 e 20: '))

    if 0 <= numero <= 5:
        print('Olha só, digitou mesmo.')

        extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')
        print(f'Você digitou o número {numero} e a forma extensa em Português dele é: {extenso[numero]}')
        
        opcao = ' '
        while opcao not in 'ns':
            opcao = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]

        if 'n' in opcao:
            print('Ok, desligando.')
            break
        
        elif 's' in opcao:
            print('Ok, vamos lá novamente!')
            continue

    else:
        print('Tente novamente, dessa vez um número no intervalo de 0 a 5, por favor.')