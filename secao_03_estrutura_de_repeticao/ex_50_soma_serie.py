"""
Exercício 50 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, 
Faça um programa que calcule o valor de H com N termos.
    
    ----------------------------------
    | EXEMPLO                         |
    ----------------------------------
    | ENTRADA:                        |
    | n = 5                           |
    | SAIDA:                          |
    | H = 2.283333333333333           |
    ----------------------------------
    

    >>> soma_serie(5)
    H = 2.283333333333333
    >>> soma_serie(7)
    H = 2.5928571428571425
    >>> soma_serie(17)
    H = 3.439552522640758
    >>> soma_serie(2)
    H = 1.5

"""


def soma_serie(n):
    """Escreva aqui em baixo a sua solução"""

    lista_cima = []
    lista_baixo = []
    contador = 1

    while contador < n+1:
        lista_cima.append(1)
        lista_baixo.append(contador)
        contador += 1


    lista_fracao = []
    contador_2 = 0

    while contador_2 < len(lista_cima):
        conta = lista_cima[contador_2]/lista_baixo[contador_2]
        lista_fracao.append(conta)
        contador_2 += 1

    soma = 0
    for item in lista_fracao:
        soma += item

    print(f'H = {soma}')