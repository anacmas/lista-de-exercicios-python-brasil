"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""

from calendar import isleap

def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""

    if data == '':
        return 'Data inválida'


    data_separada = data.split('/')
    data_em_inteiros = list(map(int, data_separada))

    if len(data_em_inteiros) != 3:
        return 'Data inválida'

    dia = data_em_inteiros[0]
    mes = data_em_inteiros[1]
    ano = data_em_inteiros[2]


    meses_31_dias = [1, 3, 5, 7, 8, 10, 12]
    meses_30_dias = [4, 6, 9, 11]
    fevereiro = [2]

    if (1 <= dia <= 31) and (1 <= mes <= 12) and (0 <= ano <= 9999):
        

        if mes in meses_31_dias:
            if dia > 31:
                return 'Data inválida'

            else: 
                return 'Data válida'

        elif mes in meses_30_dias:
            
            if dia > 30:
                return 'Data inválida'

            else: 
                return 'Data válida'
        
        elif mes == 2:
        
            if dia > 29:
                return 'Data inválida'

            elif isleap(ano):
                
                if dia > 29:
                    return 'Data inválida'
                
                else: 
                    return 'Data válida'
            
            else:
                if dia > 28:
                    return 'Data inválida'



    else:
        return 'Data inválida'





