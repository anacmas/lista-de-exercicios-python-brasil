"""
Exercício 42 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.

    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[-1, 10, 15, 20, 50, 13, 78, 22, 14, 16]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    7 número(s) entre o intervalo de zero a 25
    1 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[14, -5, 10, 2, 80, 99]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    2 número(s) entre o intervalo de zero a 25
    2 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[-55, 144, 5, 32, 18, 43, 12, 26, 76]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    3 número(s) entre o intervalo de zero a 25
    3 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[3, 5, 100, -5, 70, 88, 28, 12]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    1 número(s) entre o intervalo de zero a 25
    1 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 51 a 75
    1 número(s) entre o intervalo de 76 a 100

"""


def listar_numeros_para_avaliacao():
    """Escreva aqui em baixo a sua solução"""

    numero = 1
    intervalo_ate_25 = 0
    intervalo_ate_50 = 0
    intervalo_ate_75 = 0
    intervalo_ate_100 = 0

    while numero >= 0:
        numero = int(input('Insira um número: '))

        if 0 <= numero <= 25:
            intervalo_ate_25 +=1

        elif 26 <= numero <= 50:
            intervalo_ate_50 +=1

        elif 51 <= numero <= 75:
            intervalo_ate_75 +=1
        
        elif 76 <= numero <= 100:
            intervalo_ate_100 +=1
        
    lista = [intervalo_ate_25, intervalo_ate_50, intervalo_ate_75, intervalo_ate_100]

    contador = 0

    for intervalo in lista:

        contador += 1

        if contador == 1:
            intervalo_escrito = 'zero a 25'

        elif contador == 2:
            intervalo_escrito = '26 a 50'

        elif contador == 3:
            intervalo_escrito = '51 a 75'
        
        else: 
            intervalo_escrito = '76 a 100'


        if intervalo != 0:
            print(f'{intervalo} número(s) entre o intervalo de {intervalo_escrito}')