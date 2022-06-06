"""
Exercício 27 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o
valor a ser pago pelo cliente.
Mostre o restultado com duas casas decimais

    >>> calcular_preco_da_compra(2, 0)
    (+)  Morango  - valor:  R$  5.00 - quantidade:  2 kg - preço: R$ 2.50/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  5.00
    >>> calcular_preco_da_compra(6, 0)
    (+)  Morango  - valor:  R$ 13.20 - quantidade:  6 kg - preço: R$ 2.20/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$ 13.20
    >>> calcular_preco_da_compra(9, 0)
    (+)  Morango  - valor:  R$ 19.80 - quantidade:  9 kg - preço: R$ 2.20/kg
    (-)  Desconto - valor:  R$  1.98
              Valor Total:  R$ 17.82
    >>> calcular_preco_da_compra(0, 2)
    (+)  Maça     - valor:  R$  3.60 - quantidade:  2 kg - preço: R$ 1.80/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  3.60
    >>> calcular_preco_da_compra(0, 6)
    (+)  Maça     - valor:  R$  9.00 - quantidade:  6 kg - preço: R$ 1.50/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  9.00
    >>> calcular_preco_da_compra(0, 9)
    (+)  Maça     - valor:  R$ 13.50 - quantidade:  9 kg - preço: R$ 1.50/kg
    (-)  Desconto - valor:  R$  1.35
              Valor Total:  R$ 12.15
    >>> calcular_preco_da_compra(2, 2)
    (+)  Morango  - valor:  R$  5.00 - quantidade:  2 kg - preço: R$ 2.50/kg
    (+)  Maça     - valor:  R$  3.60 - quantidade:  2 kg - preço: R$ 1.80/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  8.60
    >>> calcular_preco_da_compra(7, 2)
    (+)  Morango  - valor:  R$ 15.40 - quantidade:  7 kg - preço: R$ 2.20/kg
    (+)  Maça     - valor:  R$  3.60 - quantidade:  2 kg - preço: R$ 1.80/kg
    (-)  Desconto - valor:  R$  1.90
              Valor Total:  R$ 17.10
    >>> calcular_preco_da_compra(7, 7)
    (+)  Morango  - valor:  R$ 15.40 - quantidade:  7 kg - preço: R$ 2.20/kg
    (+)  Maça     - valor:  R$ 10.50 - quantidade:  7 kg - preço: R$ 1.50/kg
    (-)  Desconto - valor:  R$  2.59
              Valor Total:  R$ 23.31

"""


def calcular_preco_da_compra(kilos_de_morango: int, kilos_de_maca: int):
    """Escreva aqui em baixo a sua solução"""

    if kilos_de_maca <= 5:
        preco_maca = kilos_de_maca * 1.8

    else:
        preco_maca = kilos_de_maca * 1.5


    if kilos_de_morango <= 5:
        preco_morango = kilos_de_morango * 2.5

    else:
        preco_morango = kilos_de_morango * 2.2




    if kilos_de_morango <= 5:
        preco_kg_morango = '2.50'

    else: 
        preco_kg_morango = '2.20'

    if kilos_de_maca <= 5:
        preco_kg_maca = '1.80'

    else: 
        preco_kg_maca = '1.50'



    peso_total = kilos_de_maca + kilos_de_morango
    valor_total = preco_maca + preco_morango
    desconto = valor_total*0.1
    valor_com_desconto = valor_total-(desconto)
    


    if peso_total > 8 or valor_total > 25:
        valor_utilizado = valor_com_desconto
    
    else:
        valor_utilizado = valor_total
        desconto = 0


    if kilos_de_morango == 0:
        fruta = 'Maça     '
        preco_fruta = preco_maca
        valor_do_kg = preco_kg_maca
        quantidade = kilos_de_maca

    else:
        fruta = 'Morango  '
        preco_fruta = preco_morango
        valor_do_kg = preco_kg_morango
        quantidade = kilos_de_morango


    if preco_maca > 10:
        espaco_maca = ''
    
    else:
        espaco_maca = ' '


    if preco_morango > 10:
        espaco_morango = ''
    
    else:
        espaco_morango = ' '

    if valor_utilizado > 10:
        espaco_valor_total = ''
    
    else:
        espaco_valor_total = ' '

    if preco_fruta > 10:
        espaco_fruta = ''
    
    else:
        espaco_fruta = ' '


    if kilos_de_morango == 0 or kilos_de_maca == 0:
        print(f'(+)  {fruta}- valor:  R$ {espaco_fruta}{preco_fruta:.2f} - quantidade:  {quantidade} kg - preço: R$ {valor_do_kg}/kg')
        print(f'(-)  Desconto - valor:  R$  {desconto:.2f}')
        print(f'          Valor Total:  R$ {espaco_valor_total}{valor_utilizado:.2f}')
    
    else: 
        print(f'(+)  Morango  - valor:  R$ {espaco_morango}{preco_morango:.2f} - quantidade:  {kilos_de_morango} kg - preço: R$ {preco_kg_morango}/kg')

        print(f'(+)  Maça     - valor:  R$ {espaco_maca}{preco_maca:.2f} - quantidade:  {kilos_de_maca} kg - preço: R$ {preco_kg_maca}/kg')

        print(f'(-)  Desconto - valor:  R$  {desconto:.2f}')
        print(f'          Valor Total:  R$ {espaco_valor_total}{valor_utilizado:.2f}')

