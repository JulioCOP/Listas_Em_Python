#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando
# tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves

lista= []
dados=[]
totpessoas=pesomaior=pesomenor=0
while True:
    dados.append(str(input("NOME: ")))
    dados.append(float(input("PESO: ")))
    if len(lista)==0:       #com a lista gerada, o primeiro valor é o maior e menor valores
        pesomaior=pesomenor=dados[1]
    else:   #se não, para ods demais valores informados entra a seguinte logica:
        if dados[1]>pesomaior:  #se os dados de nome e peso informados, for maior que o da primeira posição, se tornam o maior peso
            pesomaior=dados[1]
        if dados[1]<pesomenor: #em caso de valores menores, o raciocinio acima ocorre de forma inversa
            pesomenor=dados[1]
    lista.append(dados[:]) #dados são adicionados em uma lista, tanto nome quanto o peso
    dados.clear()
    resp= str(input("Deseja continuar ? [S] / [N] ")).strip().upper()[0]
    totpessoas+=1
    if resp=='N':
        break
print("="*100)
print(f"FORAM CADASTRADAS {totpessoas} pessoas")
print("="*100)
print(f"A lista gerada {lista}")
print("="*100)
print(f"O maior peso {pesomaior}Kg")
for p in lista: #para cada pessoa informada na lista
    if p[1]== pesomaior:    #a 1º pessoa na posição correspondente a posição de maior, recebe o nome de acordo com informado
        print(f"{p[0]}")
print("="*100)
print(f"O menor peso {pesomenor}Kg")
for p in lista:
    if p[1]==pesomenor:
        print(f"{p[0]}")