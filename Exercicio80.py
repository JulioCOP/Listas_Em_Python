lista=[]        #declaração da variavel lista, em que serão adicionados os valores de 0,5

for c in range(0,5):                    # para o intervalo de 0 até 5, o usuário informará
    n=int(input("Digite um número: "))  #um número que será guardado na posição "c"
    if c==0 or lista[-1]:          #SE a posição inicial (0) ou a ultima posição da lista não tiver nada
        lista.append(n)           #a posição rece o valor digitado pelo usuário
        print("Adicionado ao final da lista")  #Ou seja o prmeiro valor informado estara na primeira ou na ultima posição
    else:           #SE NÃO, para os proximos valores informados....
        pos=0
        while pos <lista[-1]:  #enquanto o valor informado, for menor do que o ultimo digitado,
                                # ocorre uma varredura de 0 a ultima posição
            if n<= lista[pos]: #para assim verificar SE o Nº inserido  é <= a ele em cada posição
                lista.insert(pos,n)   #sendo este Nº inserido menor, é adicionado um valor de acordo
                print(f"Adicionado na posição {pos} da lista")  #com sua posição correspondente em grau de tamanho.
                break
            pos+=1  #para ocorrer a varredura de posição em posição

print(f"Os valores digitados em ordem {lista}")

