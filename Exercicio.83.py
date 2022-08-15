#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com
# os parênteses abertos e fechados na ordem correta.

e=str(input("Digite uma expressão: "))
lista=[]
for simbolo in e:   #TOODA STR é uma lista, ou seja, PARA CADA EXPRESSÃO PEGA UM SIMBOLO DA EXPRESSÃO INFORMADA
    if simbolo== '(': # AO INICIAR A EXPRESSÃO
        lista.append('(')   # ABRI-SE UM PARENTESE E ESSE VALOR É JOGADO NA LISTA
    elif simbolo==')':
        if len(lista)>0: #se o tamanho da lista for maior que 0 , ou seja, se não estiver vazia
            lista.pop() #o ultimo elemento será removido
        else:
            lista.append(')') #se a lista estiver vazia, adicionar um parentese fechando
            break

if len(lista)==0:       #verificar se a lista possui pares de parenteses- um abrindo e outro fechando
    print("EXPRESSÃO CORRETA")  # para o mesmo par
else:
    print("EXPRESSÃO INCORRETA")
