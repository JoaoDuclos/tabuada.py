while True:
    tn1 = input('Digite a tabuada que deseja: ')
    if not tn1.isnumeric():
        print('Valor inválido')
    else:
        n1 = int(tn1)
        x = 1
        while x <= 10:
            res = n1 * x
            print(f'{n1}x{x}={res}')
            x += 1
        else:
            print('fim da tabuada')