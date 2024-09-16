"""
Exercício 04 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento.

    >>> calcular_ano_ultrapassagem_populacional()
    'População de A, depois de 63 ano(s) será de 515033 pessoas, superando a de B, que será de 510964 pessoas'


"""

def calcular_ano_ultrapassagem_populacional() -> str:
    """Escreva aqui em baixo a sua solução"""


    populacao_A = 80_000
    crescimento_A = 1.03

    populacao_B = 200_000
    crescimento_B = 1.015

    contador_anos = 0

    while populacao_A < populacao_B:
        contador_anos +=1
        populacao_A *= crescimento_A

        populacao_B *= crescimento_B

    return f'População de A, depois de {contador_anos} ano(s) será de {int(populacao_A)} pessoas, superando a de B, que será de {int(populacao_B)} pessoas'