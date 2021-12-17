def cpf_gerar(a=1):
    """
    Author: Wallace Wictchen
    Gera CPFs válidos 'ilimitados'
    :param a: (amount) quantidade de CPF a serem gerados
    :return: Números de CPFs com a formatação pronta
    """
    cpf = list()
    for qua in range(a):
        while True:
            from random import randint
            gerar = list()
            for n in range(11):
                gerar.append(randint(0, 9))
            digit1 = False
            digit2 = False
            for cont in range(9, 11):
                num = list()
                m = cont + 1  # Multiplication
                for c in gerar[:cont]:
                    num.append(int(c) * m)
                    m -= 1
                calc = 11 - (sum(num) % 11)
                if calc >= 10:
                    calc = 0
                if cont == 9 and calc == int(gerar[-2]):  # Verifica penútimo dígito
                    digit1 = True
                elif cont == 10 and calc == int(gerar[-1]):  # Verifica último dígito
                    digit2 = True
            if digit1 and digit2:
                cpf.append(
                    str(gerar[0]) + str(gerar[1]) + str(gerar[2]) +
                    str('.') + str(gerar[3]) + str(gerar[4]) + str(gerar[5]) +
                    str('.') + str(gerar[6]) + str(gerar[7]) + str(gerar[8]) +
                    str('-') + str(gerar[9]) + str(gerar[10])
                )
                break
    return cpf


# main program
amount = int(input('Quantos CPFs você quer gerar? '))
cpfs = cpf_gerar(amount)
for c in cpfs:
    print(f'CPF: {c}')
