"""
Exercício 45 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma com uma casa decimal.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

    >>> corrigir(('Renzo','A','B','C','D','E','E','D','C','B','A' ))
    Aluno                 Nota
    Renzo                 10
    ---------------------------
    Média geral: 10.0
    Maior nota: 10
    Menor nota: 10
    Total de Alunos: 1
    >>> corrigir(
    ... ('Renzo','A','B','C','D','E','E','D','C','B','A' ),
    ... ('Fulano','A','B','C','D','E','E','D','C','B','B' ),
    ... )
    Aluno                 Nota
    Renzo                 10
    Fulano                 9
    ---------------------------
    Média geral: 9.5
    Maior nota: 10
    Menor nota: 9
    Total de Alunos: 2
"""

def corrigir(*provas):
    """Escreva aqui em baixo a sua solução"""


    print('Aluno                 Nota')

    nota_geral = 0

    lista_notas = []

    for aluno in provas:
        pontos = 0
        contador = 1

        while contador < 11:

            if contador == 1 or contador == 10:
                resposta = 'A'

            elif contador == 2 or contador == 9:
                resposta = 'B'
            
            elif contador == 3 or contador == 8:
                resposta = 'C'
            
            elif contador == 4 or contador == 7:
                resposta = 'D' 

            elif contador == 5 or contador == 6:
                resposta = 'E'


            if aluno[contador] == resposta:
                pontos += 1

            contador += 1
            
        lista_notas.append(pontos)
        
        
        nota_geral += pontos

        
        if len(aluno[0]) == 5:
            espaco = ' '
        
        else: espaco = ''

        if pontos == 10:
            espaco_pontos = ''
        
        else:
            espaco_pontos = ' '

        print(f'{aluno[0]}{espaco}                {espaco_pontos}{pontos}')


    for nota in lista_notas:
        nota_mais_alta = lista_notas[0]
        nota_mais_baixa = lista_notas[0]

        if nota > nota_mais_alta:
            nota_mais_alta = nota
        
        if nota < nota_mais_baixa:
            nota_mais_baixa = nota


    media_geral = nota_geral /len(provas)


    print('---------------------------')
    print(f'Média geral: {media_geral}')
    print(f'Maior nota: {nota_mais_alta}')
    print(f'Menor nota: {nota_mais_baixa}')
    print(f'Total de Alunos: {len(provas)}')