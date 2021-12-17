def cpf_validade(cpf_cru):
    """
    Author: Wallace Wictchen
    Checa a validade de um CPF de acordo com o algorítimo padrão
    :param cpf_cru: Recebe o CPF de qualquer jeito
    :return: Mensagem 'CPF Válido' ou 'CPF Inválido'
    """
    cpf = cpf_cru.replace('.', '').replace('-', '')
    if not cpf.isdigit() or len(cpf) != 11 or cpf == cpf[0] * len(cpf):
        return 'Valores inválidos. Tente novamente!'
    else:
        digit1 = False
        digit2 = False
        for cont in range(9, 11):
            num = list()
            m = cont + 1  # Multiplication
            for c in cpf[:cont]:
                num.append(int(c) * m)
                m -= 1
            calc = 11 - (sum(num) % 11)
            if calc >= 10:  # Regra do algorítimo
                calc = 0
            if cont == 9 and calc == int(cpf[-2]):  # Verifica penútimo dígito
                digit1 = True
            elif cont == 10 and calc == int(cpf[-1]):  # Verifica último dígito
                digit2 = True
        return 'CPF VÁLIDO!' if digit1 and digit2 else 'CPF INVÁLIDO!'


# main program
while True:
    cpf_usr = str(input('Digite o CPF: ')).strip()
    cpf = cpf_validade(cpf_usr)
    print(cpf)
    if cpf[:3] == 'CPF':
        break
