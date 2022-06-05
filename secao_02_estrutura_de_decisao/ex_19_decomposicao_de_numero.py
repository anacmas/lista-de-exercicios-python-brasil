"""
Exercício 19 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

    >>> decompor_numero(1000)
    'O número precisa ser menor que 1000'
    >>> decompor_numero(-1)
    'O número precisa ser positivo'
    >>> decompor_numero(326)
    '326 = 3 centenas, 2 dezenas e 6 unidades'
    >>> decompor_numero(300)
    '300 = 3 centenas'
    >>> decompor_numero(100)
    '100 = 1 centena'
    >>> decompor_numero(320)
    '320 = 3 centenas e 2 dezenas'
    >>> decompor_numero(310)
    '310 = 3 centenas e 1 dezena'
    >>> decompor_numero(305)
    '305 = 3 centenas e 5 unidades'
    >>> decompor_numero(301)
    '301 = 3 centenas e 1 unidade'
    >>> decompor_numero(311)
    '311 = 3 centenas, 1 dezena e 1 unidade'
    >>> decompor_numero(111)
    '111 = 1 centena, 1 dezena e 1 unidade'
    >>> decompor_numero(101)
    '101 = 1 centena e 1 unidade'
    >>> decompor_numero(25)
    '25 = 2 dezenas e 5 unidades'
    >>> decompor_numero(20)
    '20 = 2 dezenas'
    >>> decompor_numero(21)
    '21 = 2 dezenas e 1 unidade'
    >>> decompor_numero(10)
    '10 = 1 dezena'
    >>> decompor_numero(16)
    '16 = 1 dezena e 6 unidades'
    >>> decompor_numero(1)
    '1 = 1 unidade'
    >>> decompor_numero(7)
    '7 = 7 unidades'

"""

import math

def decompor_numero(numero: int):
    """Escreva aqui em baixo a sua solução"""

    unidade_str = 'unidade'
    unidades_str = 'unidades'

    dezena_str = 'dezena'
    dezenas_str = 'dezenas'

    centena_str = 'centena'
    centenas_str = 'centenas'
    

    if 10 <= numero <= 99:
        dezena = numero // 10
        unidade = numero % 10

    elif 100 <= numero <= 999:
        centena = numero // 100
        dezena = (numero-centena) // 10
        unidade = numero % 10







    if 0 > numero:
        print('O número precisa ser positivo')

    elif 1 == numero:
        print(f'{numero} = {numero} unidade')

    elif 2 <= numero <= 9:
        print(f'{numero} = {numero} unidades')
    
    elif 10 <= numero <= 99:
        dezena = numero // 10
        unidade = numero % 10

        if dezena == 1:
            
            if unidade > 1:
                print(f'{numero} = {dezena} dezena e {unidade} unidades')
            else:
                print(f'{numero} = {dezena} dezena e {unidade} unidade')

        else:
            print(f'{numero} = {dezena} dezenas e {unidade} unidades')

    elif 100 <= numero <= 999:
        centena = numero // 100
        dezena = (numero-centena) // 10
        unidade = numero % 10
        print(f'{numero} = {centena} centenas, {dezena} dezena e {unidade} unidades')

        else:
            print(f'{numero} = {dezena} dezenas e {unidade} unidades')


    else: 
        print('O número precisa ser menor que 1000')