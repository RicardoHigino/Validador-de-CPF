print('---------------Validador de CPF---------------\n'
      '------Insira os valores com ponto e traço-----\n'
      '')
cpf = input('Digite seu CPF: ')
#    Code para formatar o cpf
ponto = cpf.replace('.', '')
traco = ponto.replace('-', '')
#    Code para primeira verificação (penúltimo número do cpf)
lista = [0, 0, 0, 0, 0, 0, 0, 0, 0]
if traco == '11111111111' or traco == '00000000000':
    print(f'{cpf} \033[31mCPF inválido!\033[m')
else:
    for e, r in enumerate(range(10, 1, -1)):
        conversao = int(ponto[e])
        valor = conversao * r
        lista[e] = valor
    resultado = lista[0] + lista[1] + lista[2] + lista[3] + lista[4] + lista[5] + lista[6] + lista[7] + lista[8]
    conta = 11 - (resultado % 11)

    if conta > 9:
        conta = 0
    #    Code para segunda verificação (último número do cpf)
    lista2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for e, r in enumerate(range(11, 2, -1)):
        conversao2 = int(ponto[e])
        valor2 = conversao2 * r
        lista2[e] = valor2
        if e == 8:
            valorcpf = int(cpf[12])
            calculo2 = valorcpf * 2
            resultado2 = lista2[0] + lista2[1] + lista2[2] + lista2[3] + lista2[4] + lista2[5] + lista2[6] + lista2[7] + \
                         lista2[8] + calculo2
            conta2 = 11 - (resultado2 % 11)
            if conta2 > 9:
                conta2 = 0
            #    Avaliação final
            cpf2 = traco[0:9]
            novo_cpf = cpf2 + str(conta) + str(conta2)
            if traco == novo_cpf:
                print(f'{cpf} \033[32mCPF Válido')
            else:
                print(f'{cpf} \033[31mCPF Inválido')
