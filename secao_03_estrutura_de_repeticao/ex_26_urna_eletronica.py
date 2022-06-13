"""
Exercício 26 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

uma eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar
 e ao final mostrar o número de votos de cada candidato.

    >>> calcular_votos()
    Votantes: 0
    Votos no candidato corrupto: 0
    Votos no candidato mentiroso: 0
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto')
    Votantes: 1
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 0
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto', 'mentiroso')
    Votantes: 2
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 1
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto', 'mentiroso', 'rouba, mas faz')
    Votantes: 3
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 1
    Votos no candidato rouba, mas faz: 1
    >>> calcular_votos('corrupto', 'mentiroso', 'rouba, mas faz', 'corrupto', 'mentiroso', 'rouba, mas faz')
    Votantes: 6
    Votos no candidato corrupto: 2
    Votos no candidato mentiroso: 2
    Votos no candidato rouba, mas faz: 2

"""


def calcular_votos(*votos):
    """Escreva aqui em baixo a sua solução"""

    contador_corrupto = 0
    contador_mentiroso = 0
    contador_rouba = 0

    numero_votantes = len(votos)

    print(f'Votantes: {numero_votantes}')

    for voto in votos:
        if voto == 'corrupto':
            contador_corrupto += 1

        elif voto == 'mentiroso':
            contador_mentiroso += 1

        else:
            contador_rouba += 1
        
    print(f'Votos no candidato corrupto: {contador_corrupto}')
    print(f'Votos no candidato mentiroso: {contador_mentiroso}')
    print(f'Votos no candidato rouba, mas faz: {contador_rouba}')