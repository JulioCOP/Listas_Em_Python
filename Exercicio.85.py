# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
# em uma lista única que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.

#lista=[]
#valores_par=[]
#valores_impares=[]
#for valores in range (0,7):
#    n=int(input(f"Digite o {valores+1}º valor: "))
#    lista.append(n)
#    if n%2==0:
#        valores_par.append(n)
#    else:valores_impares.append(n)

#print("VALORES PARES: ")
#print(f"{valores_par}")
#print()
#print("VALORES ÍMPARES: ")
#print(f"{valores_impares}")

lista=[[],[]]
valor=0
for c in range (0,7):
    valor=int(input(f"Digite o {c+1}º número: "))
    if valor%2==0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f"A lista informada pelo usuário é {lista}")
print("VALORES PARES: ")
lista[0].sort()
print(lista[0])
print("VALORES ÍMPARES: ")
lista[1].sort()
print(lista[1])

