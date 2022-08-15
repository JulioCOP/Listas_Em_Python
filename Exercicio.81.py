#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista=[]
soma=numero5=0
while True:
    n=int(input("Digite um valor: "))
    lista.append(n)
    soma+=1
    resp=str(input("Deseja continuar ? [S] / [N] ")).strip().upper()[0]
    if resp not in 'SN':
        resp=str(input("RESPOSTA INCORRETA !"
                       "\nDeseja continuar ? [S] / [N] " )).strip().upper()[0]
    else:
        if resp=='N':
            break



print(f"A lista gerada é \033[1;35m{lista}\033[m")
print(f"Foram digitados para essa lista \033[1;32m{soma}\033[m valores")
print(f"Os valores em ordem crescente \033[1;36m{sorted(lista)}\033[m")
lista.sort(reverse= True)
print(f"Os valores em ordem decrescente \033[1;33m{lista}\033[m")
if 5 in lista:
    print("\033[1mNa lista informada pelo usuário, contem o número 5\033[m")

else:
    print("\033[1mNa lista não contem o número 5\033[m")

print('\n\033[1;31mFIM DO PROGRAMA\033[m')