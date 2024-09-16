"""
Exercício 31 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

FO Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de
valores referentes aos preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra.
Um valor -1 deve ser informado pelo operador para finalizar o programas
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então
calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra.

    >>> from secao_03_estrutura_de_repeticao import ex_31_conveniencia_manuel
    >>> entradas = ['-1']  # Encerrando o programa sem nenhuma compra
    >>> ex_31_conveniencia_manuel.input = lambda k: entradas.pop()
    >>> ex_31_conveniencia_manuel.rodar_programa_de_caixa()
    Lojas Tabajara
    -------------------
    Programa encerrado!
    >>> entradas = ['2.00', '-1', '1.99']  # Compra de apenas um produto
    >>> ex_31_conveniencia_manuel.input = lambda k: entradas.pop()
    >>> ex_31_conveniencia_manuel.rodar_programa_de_caixa()
    Lojas Tabajara
    Total     : R$   1.99
    Dinheiro  : R$   2.00
    Troco     : R$   0.01
    -------------------
    Programa encerrado!
    >>> entradas = ['5.00', '-1', '1.99', '1.99']  # Compra de dois produtos
    >>> ex_31_conveniencia_manuel.input = lambda k: entradas.pop()
    >>> ex_31_conveniencia_manuel.rodar_programa_de_caixa()
    Lojas Tabajara
    Total     : R$   3.98
    Dinheiro  : R$   5.00
    Troco     : R$   1.02
    -------------------
    Programa encerrado!
    >>> entradas = ['10.00', '-1', '5.35', '5.00', '0', '1.98', '1.99']  # Compra de dois produtos
    >>> ex_31_conveniencia_manuel.input = lambda k: entradas.pop()
    >>> ex_31_conveniencia_manuel.rodar_programa_de_caixa()
    Lojas Tabajara
    Total     : R$   3.97
    Dinheiro  : R$   5.00
    Troco     : R$   1.03
    -------------------
    Lojas Tabajara
    Total     : R$   5.35
    Dinheiro  : R$  10.00
    Troco     : R$   4.65
    -------------------
    Programa encerrado!

"""


def rodar_programa_de_caixa():
    """Escreva aqui em baixo a sua solução"""

    def espacos(valor):
        if valor >= 10:
            return ''
        
        
        return ' '



    tracos = '-------------------'
    print('Lojas Tabajara')

    entrada = -2
    



    while entrada != -1:
        total = 0

        if entrada == -2:
            total = 2

        while entrada != 0 and entrada != -1:
            total += entrada
            entrada = float(input('Insira uma entrada: '))

        if entrada == 0:
            pagamento = float(input('Insira o dinheiro do pagamento: '))
            troco = pagamento - total
            print(f'Total     : R$   {total:.2f}')
            print(f'Dinheiro  : R$  {espacos(pagamento)}{pagamento:.2f}')
            print(f'Troco     : R$   {troco:.2f}')
            print(tracos)
            print('Lojas Tabajara')
            entrada = float(input('Insira uma entrada: '))

    if total != 0:
        pagamento = float(input('Insira o dinheiro do pagamento: '))
        troco = pagamento - total
        print(f'Total     : R$   {total:.2f}')
        print(f'Dinheiro  : R$  {espacos(pagamento)}{pagamento:.2f}')
        print(f'Troco     : R$   {troco:.2f}')
    print(tracos)
    print('Programa encerrado!')


















    # tracos = '-------------------'
    # entrada = float(input('Insira uma entrada: '))
    # total_compra = 0
    # lista = []

    # while entrada != '-1':

    #     if entrada != 0:
    #         total_compra += entrada
            
    #     else:
    #         lista.append(total_compra)
    #         print(tracos)
    #         print('Lojas Tabajara')
    #         total_compra = 0

    #     entrada = float(input('Insira uma entrada: '))

    # lista.append(total_compra)


    # valor_dado = float(input('Insira o dinheiro do pagamento: '))

    # print('Lojas Tabajara')
    # print(f'Total     : R$   {total_compra}')
    # print(tracos)
    # print('Programa encerrado!')












    # print('Lojas Tabajara')

    # str_tracos = '-------------------'
    # str_encerrar = 'Programa encerrado!'
    # lista_precos = []

    # while True:
    #     operacao = float(input('Insira o valor do produto ou número da operação: '))

    #     if operacao == -1 :
    #         print(str_tracos)
    #         print(str_encerrar)
    #         break

    #     if operacao == 0:
    #         print(str_tracos)


    #     if operacao != 0 and operacao !== 1:
    #         lista_precos.append(operacao)
