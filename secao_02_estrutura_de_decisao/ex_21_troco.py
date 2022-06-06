"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""

    contador_notas_de_100 = 0
    contador_notas_de_50 = 0
    contador_notas_de_10 = 0
    contador_notas_de_1 = 0

    while True:
        if valor >= 100:
            contador_notas_de_100 += 1
            valor -= 100

        elif valor >= 50:
            contador_notas_de_50 += 1 
            valor -= 50
        
        elif valor >= 10:
            contador_notas_de_10 += 1
            valor -= 10

        elif valor >= 5:
            contador_notas_de_5 += 1
            valor -= 5

        elif valor >= 1:
            contador_notas_de_1 += 1
            valor -= 1
        
        if valor == 0:
            break
    
        if contador_notas_de_1 == 1:
            notas = 'nota'
        else: 
            notas = 'notas'


        if contador_notas_de_5 == 1:
            notas = 'nota'
        else: 
            notas = 'notas'


        if contador_notas_de_10 == 1:
            notas = 'nota'
        else: 
            notas = 'notas'

        if contador_notas_de_50 == 1:
            notas = 'nota'
        else: 
            notas = 'notas'


        if contador_notas_de_100 == 1:
            notas = 'nota'
        else: 
            notas = 'notas'

        # if valor == 1:
        #     contador = contador_notas_de_1
        
        # elif valor == 5:
        #     contador = contador_notas_de_5

        # elif valor == 10:
        #     contador = contador_notas_de_10
        
        # elif valor == 50:
        #     contador = contador_notas_de_50

        # else:
        #     contador = contador_notas_de_100

        
        if (contador_notas_de_1 > 0) :

            if (contador_notas_de_1 > 1) :
                plural = "s"
            else:
                plural = ""

            nota_de_1 =  f'{contador_notas_de_1} nota{plural} de R$ {valor}'
        else:
            nota_de_1 = ""

        if (contador_notas_de_10 > 1) :
            plural = "s"
        else:
            plural = ""

        nota_de_10 =  f'{contador_notas_de_10} nota{plural} de R$ {valor}'

        retorno = ""

        if nota_de_10 != "":
            if len(retorno) > 0:
                retorno.concat("," + nota_de_10)
            else:
                retorno.concat(nota_de_10)

        return nota_de_1 + nota_de_10

        if valor == 1 or valor == 5 or valor == 10 or valor == 50 or valor == 100:
            return  f'{contador} {notas} de R$ {valor}'

        

        if contador_notas_de_100 != 0:
            print(f'{contador_notas_de_100} {notas} de R$ 100')
        
        if contador_notas_de_50 != 0:
            print(f'{contador_notas_de_100} {notas} de R$ 100')








    # notas = [1, 5, 10, 50, 100]
    # pedacos=[]
    # total = valor




    # if valor >= 100:
    #     contador_notas_100 = 0

    #     while total >= 100:
    #         contador_notas_100 += 1
    #         total = total - 100

    # if (total - (contador_notas_100 * 100)) >= 50:
    #     numero_notas_50 = 1







    # A = 1

    # valor_separado = []

    # for i in range(0, len(valor_string), A):
    #     valor_separado.append(int(valor_string[i : i + A]))

    # unidade = valor_separado[-1]

    # if valor > 9: 
    #     dezena = valor_separado[-2]

    #     if dezena >= 50:
    #         numero_de_notas_de_50 = 1
    #         troco_de_notas_de_50 = dezena - 50

    #         if troco_de_notas_de_50 >= 10:
    #             numero_notas_de_10 = troco_de_notas_de_50//10
    #             troco_de_notas_de_10 = troco_de_notas_de_50 - numero_notas_de_10

    #             if troco_de_notas_de_10 >= 5:
    #                 numero_notas_de_5 = troco_de_notas_de_10//5
    #                 troco_de_notas_de_5 = troco_de_notas_de_10 - numero_notas_de_5
                
    #                 if troco_de_notas_de_5 >= 1:
    #                     numero_notas_de_1 = troco_de_notas_de_5//1

    #             else:
    #                 numero_notas_de_1 = troco_de_notas_de_5//1

    
    # if valor > 99:
    #     centena = valor_separado[-3]
    #     numero_notas_de_100 = centena

    



##--------------------



    # if valor >= 100:
    #     numero_de_notas_de_100 = valor//100
    #     troco_de_100 = valor % 100 

    #     if troco_de_100 >= 50:
    #         numero_de_notas_de_50 = troco_de_100//50
    #         troco_de_50 = troco_de_100 % 50


    #         if troco_de_50 >= 10:
    #             numero_de_notas_de_10 = troco_de_50//10
    #             troco_de_10 = troco_de_50 % 10

    #         elif troco_de_10 >= 5:
    #             numero_de_notas_de_5 = troco_de_10//5
    #             troco_de_5 = troco_de_10 % 5
    #             numero_de_notas_de_1 = troco_de_5
            
    #         else: 
    #             numero_de_notas_de_1 = troco_de_10

    #     else: 
    #         if troco_de_10 >= 5:
    #             numero_de_notas_de_5 = troco_de_10//5
    #             troco_de_5 = troco_de_10 % 5
    #             numero_de_notas_de_1 = troco_de_5
            
    #         else: 
    #             numero_de_notas_de_1 = troco_de_10










    # notas = [1, 5, 10, 50, 100]
    # pedacos=[]
    # resto = valor
    
    # while resto > 0:
    #     tipo_de_nota = notas.pop()
    # if len(pedacos)==1:
    #     return pedacos.pop()






