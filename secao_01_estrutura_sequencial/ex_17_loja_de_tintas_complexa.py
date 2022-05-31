"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""
import math

def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""

    metros = float(input('Quantos m² tem a área a ser pintada? '))
    litro_por_m2 = metros/6
    litro_por_m2_arredondado = math.ceil(litro_por_m2*1.1)
    print(f'Você deve comprar {litro_por_m2_arredondado} litros de tinta.')

    #só 18 litos:
    numero_latas_18 = math.ceil(litro_por_m2/18)
    preco_18 = numero_latas_18 * 80
    sobrar_18 = (numero_latas_18*18)-(litro_por_m2)
    print(f'Você pode comprar {numero_latas_18} lata(s) de 18 litros a um custo de R$ {preco_18}. Vão sobrar {sobrar_18} litro(s) de tinta.')

    #Só 3.6 litros:
    numero_latas_3 = round(litro_por_m2/3.6)
    preco_3 = numero_latas_3 * 25
    sobrar_3 = (numero_latas_3*3.6)-(litro_por_m2)
    print(f'Você pode comprar {numero_latas_3} lata(s) de 3.6 litros a um custo de R$ {preco_3}. Vão sobrar {sobrar_3} litro(s) de tinta.')

    #melhor combinação:
    if litro_por_m2 < 10.8:
        numero_latas_melhor = round(litro_por_m2/3.6)
        sobrar_melhor = (numero_latas_melhor*3.6) - litro_por_m2
        print(f'Para menor custo, você pode comprar 0 lata(s) de 18 litros e {numero_latas_melhor} galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.')

calcular_latas_e_preco_de_tinta()

    #if 0 < litro_por_m2 <= 18:
     #   print("Você deve comprar 1 lata(s) tinta ao custo de R$ 80.00")

   # else:
    #    numero_de_latas = round(litro_por_m2/18)
    #    preco = numero_de_latas * 80
      #  print('Você deve comprar', numero_de_latas, 'lata(s) tinta ao custo de R$ %.2f' %(preco))
