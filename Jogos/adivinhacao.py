print("*********************************")
print("Bem vindo ao jogo de adivinhação")
print("*********************************")

numero_secreto = 55
tentativas = 3
count = 1

while (count <= tentativas) :
    print("Tentativa : {} de {}".format(count, tentativas ))

    chute = input("Digite um número: ")
    chute = int(chute)

    print("Você digito",":", chute)

    count = count + 1

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if ( acertou ):
        print("Você acertou")
        break
    else:
        if ( maior ):
            print("Você errou: o valor chutado foi maior")
        elif ( menor ):
            print("Você errou: o valor chutado foi menor")
        else:
            print("Ops!!")


print("Fim do Jogo")