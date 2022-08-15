#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
#qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

valor=[]
maior=menor=0
for c in range(0,5):
    valor.append(int(input(f"Digite um número para a posição {c}: ")))
    if c==0:
        maior=menor=valor[c]  #primeiro valor informado é o menor e o maior valor
    else:
        if valor[c]>maior:
            maior=valor[c]
        else:
            menor=valor[c]
print("-"*150)
print(f"\n\033[1;30;31mLISTA: {valor}\033[m", end=" ")
print(f"\nO maior valor digitado para a lista acima é \033[1;35m{maior}\033[m e sua(s) posição(ões)")
for i,v in enumerate(valor):
    if v==maior:
        print(f"\033[1;35m{i}\033[m", end=" ")

print(f"\nO menor valor digitado para a lista é \033[1;36m{menor}\033[m e sua(s) posição(ões")
for i,v in enumerate(valor):
    if v==menor:
        print(f"\033[1;36m{i}\033[m", end=" ")





