"""
Exercício 38 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
1) Esse funcionário foi contratado em 2018;
2) Em 2019 recebeu aumento de 1,5% sobre seu salário inicial;
3) A partir de 2020 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine a evolução salarial do funcionário em 5 anos

Os valores devem ser exibidos com duas casas decimais

    >>> calcular_salarios_anuais(1000)
    Salário em 2018: R$ 1000.00
    Salário em 2019: R$ 1015.00. Aumento porcentual: 1.50%
    Salário em 2020: R$ 1045.45. Aumento porcentual: 3.00%
    Salário em 2021: R$ 1108.18. Aumento porcentual: 6.00%
    Salário em 2022: R$ 1241.16. Aumento porcentual: 12.00%
    Salário em 2023: R$ 1539.04. Aumento porcentual: 24.00%
    >>> calcular_salarios_anuais(1500)
    Salário em 2018: R$ 1500.00
    Salário em 2019: R$ 1522.50. Aumento porcentual: 1.50%
    Salário em 2020: R$ 1568.17. Aumento porcentual: 3.00%
    Salário em 2021: R$ 1662.27. Aumento porcentual: 6.00%
    Salário em 2022: R$ 1861.74. Aumento porcentual: 12.00%
    Salário em 2023: R$ 2308.55. Aumento porcentual: 24.00%
    
"""


def calcular_salarios_anuais(salario: float):
    """Escreva aqui em baixo a sua solução"""

    ano = 2019
    aumento_em_porcentagem = 1.5
    aumento = 1.015

    contador = 2019

    salario_ano = salario

    print(f'Salário em {ano-1}: R$ {salario:.2f}')

    while contador < (ano + 5):

        salario_ano = salario_ano * aumento

        print(f'Salário em {contador}: R$ {salario_ano:.2f}. Aumento porcentual: {aumento_em_porcentagem:.2f}%')
        
        aumento_em_porcentagem *= 2
        aumento = (aumento - 1) *2
        aumento += 1
        contador += 1
















    # print(f' Salário em 2018: R$ {salario:.2f}')
    
    # contador_ano = 2019
    # contador = 0

    # porcentagem_anual = 1.5
    # porcentagem_anual_dividido_por_100 = 0.015
    


    # while contador < 5:
    #     porcentagem_anual_calculo = salario + (salario*porcentagem_anual_dividido_por_100)

    #     print(f' Salário em {contador_ano}: R$ {porcentagem_anual_calculo}. Aumento porcentual: {porcentagem_anual:.2f}%')

    #     porcentagem_anual_dividido_por_100 *= 2
    #     porcentagem_anual *= 2
    #     contador_ano += 1
    #     contador += 1