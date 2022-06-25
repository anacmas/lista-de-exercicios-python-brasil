"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_37_senso_de_academia
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""


def rodar_senso():
    """Escreva aqui em baixo a sua solução"""

    lista = []

    nome = str(input('Nome: '))

    while nome != '0':
        altura = int(input('Altura: '))
        peso = int(input('Peso: '))
        lista.append((nome, altura, peso))
        nome = str(input('Nome: '))


    mais_alto = 0
    mais_baixo = 999
    maior_altura = 0
    menor_altura = 999

    mais_gordo = 0
    mais_magro = 999
    maior_peso = 0
    menor_peso = 999

    nome_mais_alto = ''
    nome_mais_baixo = ''
    nome_mais_gordo = ''
    nome_mais_magro = ''

    soma_alturas = 0
    soma_pesos = 0

    for pessoa in lista:
        
        if pessoa[1] > maior_altura:
            maior_altura = pessoa[1]
            nome_mais_alto = pessoa[0]
        
        if pessoa[1] < menor_altura:
            menor_altura = pessoa[1]
            nome_mais_baixo = pessoa[0]
        
        if pessoa[2] > maior_peso:
            maior_peso = pessoa[2]
            nome_mais_gordo = pessoa[0]

        if pessoa[2] < menor_peso:
            menor_peso = pessoa[2]
            nome_mais_magro = pessoa[0]

        soma_alturas += pessoa[1]

        soma_pesos += pessoa[2]

    media_altura = soma_alturas/len(lista)
    media_peso = soma_pesos/len(lista)

        
    print(f'Cliente mais alto: {nome_mais_alto}, com {maior_altura} centímetros')
    print(f'Cliente mais baixo: {nome_mais_baixo}, com {menor_altura} centímetros')
    print(f'Cliente mais magro: {nome_mais_magro}, com {menor_peso} kilos')
    print(f'Cliente mais gordo: {nome_mais_gordo}, com {maior_peso} kilos')

    print('--------------------------------------------------')

    print(f'Media de altura dos clientes: {media_altura:.1f} centímetros')
    print(f'Media de peso dos clientes: {media_peso:.1f} kilos')


