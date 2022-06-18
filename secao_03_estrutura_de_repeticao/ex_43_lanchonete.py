"""
Exercício 43 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que receba os itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido e quantidade de itens
comprados.


    >>> fechar_conta()
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          0 |       0.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          1 |       1.20 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          1 |       1.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          3 |       3.60 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          5 |       6.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          8 |      10.70 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         12 |      15.50 |
    -----------------------------------------------------------------------------

    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('104', 5))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Cheeseburger     | 104    | 1.30                |          5 |       6.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         17 |      22.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('105', 6))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Refrigerante     | 105    | 1.00                |          6 |       6.00 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         18 |      21.50 |
    -----------------------------------------------------------------------------

"""


def fechar_conta(*itens):
    """Escreva aqui em baixo a sua solução"""

    tracos = '|---------------------------------------------------------------------------|'

    print('_____________________________________________________________________________')
    print('|                              RESUMO DA CONTA                              |')
    print(tracos)
    print('| Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |')

    if len(itens) == 0:
        zero = 0
        print(tracos)
        print(f'| Total Geral:                                    |          {zero} |       {zero:.2f} |')
        print('-----------------------------------------------------------------------------')


    else:
        contador_cachorro = 0
        contador_bauru_s = 0
        contador_bauru_o = 0
        contador_hamburguer = 0
        contador_cheeseburguer = 0
        contador_refrigerante = 0

        for item in itens:

            if item[0] == '100':
                contador_cachorro += item[1]

            elif item[0] == '101':
                contador_bauru_s += item[1]

            elif item[0] == '102':
                contador_bauru_o += item[1]

            elif item[0] == '103':
                contador_hamburguer += item[1]
            
            elif item[0] == '104':
                contador_cheeseburguer += item[1]

            else:
                contador_refrigerante += item[1]
        
        lista = [('Cachorro Quente', 100, contador_cachorro, 1.2), 
                ('Bauru Simples  ', 101, contador_bauru_s, 1.3), 
                ('Bauru com Ovo  ', 102, contador_bauru_o, 1.5), 
                ('Hamburger      ', 103, contador_hamburguer, 1.2), 
                ('Cheeseburger   ', 104, contador_cheeseburguer, 1.3),
                ('Refrigerante   ', 105, contador_refrigerante, 1)]


        contador = 0
        contador_alimento = 0
        preco_total_compra = 0
        quantidade_total_itens_compra = 0

        for item in lista:
            
            if contador == 0:
                contador_alimento = lista[0][2]

            elif contador == 1:
                contador_alimento = lista[1][2]

            elif contador == 2:
                contador_alimento = lista[2][2]
                
            elif contador == 3:
                contador_alimento = lista[3][2]
                
            elif contador == 4:
                contador_alimento = lista[4][2]
            
            elif contador == 5:
                contador_alimento = lista[5][2]

            if contador_alimento > 0:
                preco_total_por_alimento = contador_alimento * item[3]
                print(f'| {item[0]}  | {item[1]}    | {item[3]:.2f}                |          {item[2]} |       {preco_total_por_alimento:.2f} |')
                
                preco_total_compra += preco_total_por_alimento
                quantidade_total_itens_compra += item[2]

            contador += 1

        if quantidade_total_itens_compra > 9:
            espaco_quantidade = ''
        
        else: 
            espaco_quantidade = ' '

        if preco_total_compra >= 10:
            espaco_preco = ''
        
        else:
            espaco_preco = ' '

        print(tracos)
        print(f'| Total Geral:                                    |         {espaco_quantidade}{quantidade_total_itens_compra} |      {espaco_preco}{preco_total_compra:.2f} |')
        print('-----------------------------------------------------------------------------')

