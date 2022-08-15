#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
#em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente
valores=list()
while True:   #varios numeros usa while
    n=(int(input("Digite um número: ")))
    if n not in valores:
        valores.append(n)
        print("NÚMERO CADASTRADO COM SUCESSO...")
    else:
        print("NÚMERO JÁ ADICIONADO A LISTA"
              "\nLOGO, O Nº INFORMADO NÃO SERA ADICIONADO")

    resp=str(input("Deseja continuar ? [S]/[N] ")).strip().upper()[0]
    while resp not in 'SN':
        resp=str(input("Resposta incorreta..."
                       "Informe se você deseja continuar [S]/[N] ? ")).strip().upper()[0]
    if resp=='N':
        break
print(f"A lista gerada em ordem crescente foi: {sorted(valores)}", end=" ")





