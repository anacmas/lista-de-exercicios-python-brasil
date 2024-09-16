"""
Exercício 41 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1                                0
3                                10
6                                15
9                                20
12                               25

    >>> gerar_dados_de_financiamente(1000)
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1000.00      0%              1                       R$   1000.00
    R$ 1100.00      10%             3                       R$    366.67
    R$ 1150.00      15%             6                       R$    191.67
    R$ 1200.00      20%             9                       R$    133.33
    R$ 1250.00      25%             12                      R$    104.17
    >>> gerar_dados_de_financiamente(1500)
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1500.00      0%              1                       R$   1500.00
    R$ 1650.00      10%             3                       R$    550.00
    R$ 1725.00      15%             6                       R$    287.50
    R$ 1800.00      20%             9                       R$    200.00
    R$ 1875.00      25%             12                      R$    156.25

"""


def gerar_dados_de_financiamente(valor_inicial: float):
    """Escreva aqui em baixo a sua solução"""

    print('Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela')

    print(f'R$ {valor_inicial:.2f}      0%              1                       R$   {valor_inicial:.2f}')

    quant_parcelas = 3
    porcentagem = 10

    while quant_parcelas < 12:
        valor_divida = valor_inicial + (valor_inicial*(porcentagem/100))
        
        valor_parcela = valor_divida/quant_parcelas

        print(f'R$ {valor_divida:.2f}      {porcentagem}%             {quant_parcelas}                       R$    {valor_parcela:.2f}')
        quant_parcelas += 3
        porcentagem += 5



    porcentagem_25 = 25
    quant_parcelas_25 = 12

    valor_divida_25 = valor_inicial + (valor_inicial*(porcentagem_25/100))
    
    valor_parcela_25 = valor_divida_25/quant_parcelas_25

    print(f'R$ {valor_divida_25:.2f}      {porcentagem_25}%             {quant_parcelas_25}                      R$    {valor_parcela_25:.2f}')