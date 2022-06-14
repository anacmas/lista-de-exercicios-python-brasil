"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""

    soma = 0
    soma_cidade_pequena = 0
    contador = 0
    mais_acidentes = ['', 0, 0]
    menos_acidentes = ['', 0, 99999999999]

    for cidade in cidades:

        if cidade[2] > mais_acidentes[2]:
            mais_acidentes = cidade

            mais_acidentes_por_mil = (1000*cidade[2]/cidade[1])


        if cidade[2] < menos_acidentes[2]:
            menos_acidentes = cidade
            menos_acidentes_por_mil = (1000*cidade[2]/cidade[1])

    for cidade_media in cidades:
        soma += cidade_media[1]
    
    media_carros_por_cidade = soma/len(cidades)

    for cidade_pequena in cidades:
        
        if cidade_pequena[1] <= 150_000:
            soma_cidade_pequena += cidade_pequena[1]
            contador += 1
    
    media_carros_por_cidade_pequena = soma_cidade_pequena/contador

    
    print(f'O maior índice de acidentes é de {mais_acidentes[0]}, com {mais_acidentes_por_mil:.1f} acidentes por mil carros.')

    print(f'O menor índice de acidentes é de {menos_acidentes[0]}, com {menos_acidentes_por_mil:.1f} acidentes por mil carros.')

    print(f'O média de veículos por cidade é de {int(media_carros_por_cidade)}.')

    print(f'A média de acidentes total nas cidades com menos de 150 mil carros é de {media_carros_por_cidade_pequena:.1f} acidentes.')
