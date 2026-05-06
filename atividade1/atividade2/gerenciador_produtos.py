#Crie um programa com menu e repetição (while) para gerenciar uma lista de produtos de uma loja:
#Menu:
#1 - Inserir produto
#2 - Consultar produto
#3 - Remover produto
#4 - Listar todos os produtos
#5 - Sair do programa
produtos=[]
opção=0
while opção != 5:
    opção=int(input("qual sua opção"))
    if opção ==1:
        print("opção")
        nome=input("qual nome do produto?")
        produtos.append(nome)
    if opção == 2:
        nome=input("qual é o nome do produto?")
        if nome in produtos:
            print("produdo encontrado")
        else:
            print("o produto não foi encontrado")
    if opção == 3:
        nome=input("nome do produto")
        if nome in produtos:
            produtos.remove(nome)
            print("remove produto")
        else:
            print("produto não encontrado")
    if opção == 4:
        for nome in produtos:
            print("produtos:", nome)
    if opção == 5:
        print("saindo do programa")
            
