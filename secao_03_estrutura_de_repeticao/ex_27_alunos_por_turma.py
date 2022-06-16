"""
Exercício 27 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade
de alunos para cada turma. As turmas não podem ter mais de 40 alunos e devem ter ao menos um aluno.
Arredonde o valor da média para baixo.

    >>> from secao_03_estrutura_de_repeticao import ex_27_alunos_por_turma
    >>> entradas = ['1', '1']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 1
    Média de alunos por turma: 1
    >>> entradas = ['40', '40', '2']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 2
    Média de alunos por turma: 40
    >>> entradas = ['10', '20', '30', '40', '-1', '4']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 4
    Uma turma deve ter de 1 a 40 alunos, não é possível ter -1 alunos
    Média de alunos por turma: 25
    >>> entradas = ['10', '20', '30', '0', '41', '3']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 3
    Uma turma deve ter de 1 a 40 alunos, não é possível ter 41 alunos
    Uma turma deve ter de 1 a 40 alunos, não é possível ter 0 alunos
    Média de alunos por turma: 20

"""


def calcular_media_de_alunos_por_turma():
    """Escreva aqui em baixo a sua solução"""

    turmas = int(input('Número de turmas: '))
    print(f'Número de turmas: {turmas}')


    soma = 0

    for turma in range(turmas):
        aluno = int(input('Quantos alunos nessa turma? '))

        while aluno > 40 or aluno < 1:
            print(f'Uma turma deve ter de 1 a 40 alunos, não é possível ter {aluno} alunos')
            aluno = int(input('Quantos alunos nessa turma? '))

        soma += aluno
            
    media = soma/turmas

    print(f'Média de alunos por turma: {round(media)}')





    # turmas = int(input('Número de turmas: '))
    # print(f'Número de turmas: {turmas}')

    # count = 0
    # soma = 0

    # while count < turmas:
    #     aluno = int(input('Quantos alunos nessa turma? '))

    #     if aluno > 40 or aluno < 1:
    #         print(f'Uma turma deve ter de 1 a 40 alunos, não é possível ter {aluno} alunos')

    #     else:
    #         soma += aluno
        
    #     count += 1
            
    # media = soma/turmas

    # print(f'Média de alunos por turma: {round(media)}')
