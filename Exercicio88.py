#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e
# guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de
# cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

from time import sleep

lista=[]
print()
print()
sleep(1)
print("#"*7 ,"\033[1;33mBOLETIM DE NOTAS\033[m", "#"*10)
sleep(1)
while True:
    nome=(str(input('NOME DO ALUNO: ')))
    nota1=float(input("1° NOTA DO ALUNO(A): "))
    nota2=float(input("2º NOTA DO ALUNO(A): "))
    media = ((nota1 + nota2 )/ 2)
    lista.append([nome,[nota1,nota2],media])
    resp= str(input("Você deseja acionar mais algum aluno ? [S] / [N] ")).strip().upper()
    while  resp not in 'SN':
        resp = str(input("RESPOTA INCORRETA !"
                         "\nVocê deseja acionar mais algum aluno ? [S] / [N] ")).strip().upper()
    if resp=='N':
        break
print(f"{'Nº':<10} {'ALUNO':<10} {'MÉDIA':>10}")

for numero, aluno in enumerate (lista):
    print(f"\033[1m{numero:<10} {aluno[0]:<10} {aluno[2]:>10.2f}\033[m")
while True:

    print("\033[1;31m=-\033[m"*50)
    sleep(1)
    print("\033[1mUsuário, quais notas você deseja ver , de acordo com os Nºs? \033[m"
          "OU \n\033[1mDIGITE \033[1;34m-1\033[m SE DESEJAR FINALIZAR O PROGRAMA.\033[m")
    nota_aluno=int(input())
    if nota_aluno==-1:
        break
    if nota_aluno<= len(lista)-1:
# len(ficha) é a quantidade de alunos cadastrados ou inseridos na lista
#para este comando =  o usuário selecina um valor de 0 até o determinando números de itens que possui a lista
# e assim é mostrado as notas do aluno desejado, de acordo com a posição escolhida.
# ex: Se o usuário estiver digitado Pedro na 2º posição (1 para o python), será mostrado suas duas notas
        print(f"Notas de \033[1;35m{lista[nota_aluno][0]}\033[m são \033[1;35m{lista[nota_aluno][1]}\033[m")

sleep(1)
print("\033[1mFINALIZANDO O PROGRAMA\033[m")