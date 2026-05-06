# faculdade-python
Atividades e projetos feitos em Python na facudade.

Exercício 06:
#Crie um programa com um menu (repetição):
#1-Inserir Aluno
#2-Consultar Aluno
#3-Remover Aluno
#4-Consultar a lista completa
#5-Sair do programa
alunos=[]
opção=0
while opção != 5:
    opção=int(input("qual é sua opção"))
    if opção == 1:
        print("opção")
        nome=input("qual é seu nome?")
        alunos.append(nome)
    if opção == 2:
        nome=input("nome do nome")
        if nome in alunos:
            print("nome encontrado")
        else:
            print("nome não encontrado")
    if opção == 3:
        nome=input("nome do aluno")
        if nome in alunos:
            alunos.remove(nome)
            print("nome removido:", nome)
        else:
            print("o nome não encontrado:", nome)
    if opção ==4:
        for nome in alunos:
         print("aluno:", nome)
         if opção ==5:
             print("saindo do programa")
