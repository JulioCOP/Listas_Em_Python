#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista1=[]
lista2=[]
lista3=[]
while True:
    n=int(input("Informe um número: "))
    lista1.append(n)
    if n % 2 == 0:
        lista2.append(n)
    else:
        lista3.append(n)

    resp=(str(input("Deseja conntinuar ? [S] / [N] "))).strip().upper()[0]
    if resp=='N':
        break



print(f"Lista informada pelo usuário é {lista1}")
print(f"A segunda lista é {lista2} e sÓ contem Nºs PARES")
print(f"A terceira lista {lista3} e só contem Nºs ÍMPARES")