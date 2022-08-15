#Exercício Python 086 e 087: Crie um programa que declare uma matriz de dimensão 3×3
#e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela,
#com a formatação correta.
#Aprimore, mostrando:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

from time import sleep
print()
print("#"*100)
n=int(input("\033[1mInforme a ordem da matriz:\033[m "))
mat:[[int]]=[[0 for x in range (n)]for x in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][j]=int(input(f"Digite um valor para {[i],[j]}: "))
sleep(0.5)
print("\033[1;32mA MATRIZ:\033[m")
sleep(0.5)

for i in range(n):
    for j in range (n):
        print(f"\033[1;31m{mat[i][j]:^5}\033[m", end=" ")
    print()
print("="*100)

soma=0
for i in range(n):
    for j in range(n):
        if mat[i][j] % 2==0:
            soma+=mat[i][j]
sleep(0.5)
print(f"A SOMA DOS VALORES PARES DA MATRIZ É \033[1;30m{soma}\033[m")
print("="*100)
print("\033[1m 3º COLUNA DA MATRIZ: ")
sleep(0.5)

soma_coluna=0
for i in range (n):
    for j in range(n):
        if j==2:
            print(f'\033[1;31m{mat[i][j]:^5}\033[m', end=' ')
            soma_coluna+=mat[i][j]
sleep(0.5)
print(f"\nA soma da 3º coluna é \033[1;36m{soma_coluna}\033[m")
sleep(0.5)

print("="*100)
print("\033[1;33mVALORES DA 2º LINHA:\033[m ")

for i in range(n):
    for j in range(n):
        if i==1:
            sleep(0.5)
            print(f"\033[1;34m{mat[i][j]:^5}\033[m", end=" ")
print()
sleep(1.5)
print("\n\033[1;35mFIM\033[m", end=" ")
sleep(1)
print("\033[1;35mDO\033[m",end=" ")
sleep(1)
print("\033[1;35mPROGRAMA\033[m", end=" ")
sleep(1.5)
print()