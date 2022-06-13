"""
Exercício 11 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao


Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido.
Também mostre a soma dos números da sequência.

    >>> calcular_numeros_no_intervalo_e_somar(1, 10)
    'Sequência: 1, 2, 3, 4, 5, 6, 7, 8, 9. Soma: 45'
    >>> calcular_numeros_no_intervalo_e_somar(-10, -1)
    'Sequência: -10, -9, -8, -7, -6, -5, -4, -3, -2. Soma: -54'
    >>> calcular_numeros_no_intervalo_e_somar(-1, -10)
    'Sequência: vazia. Soma: 0'

"""

import math
from operator import contains

def calcular_numeros_no_intervalo_e_somar(inicio: int, fim: int) -> str:
    """Escreva aqui em baixo a sua solução"""

    if inicio > fim:
        return 'Sequência: vazia. Soma: 0'


    else:

        lista = [inicio, '']
        contador = inicio


        while contador < fim-1:
            contador += 1
            lista.insert(-1, contador)

        lista.pop()


        contador_2 = 0
        contador_lista = 0

        while contador_2 < len(lista):
            contador_lista += lista[contador_2]
            contador_2 += 1
        

        print(f"'Sequência: ", end="")
        print(*lista, sep = ', ', end="")
        print(f". Soma: {contador_lista}'")
