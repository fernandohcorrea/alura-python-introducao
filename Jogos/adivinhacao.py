import random;

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000
    nivel = 0
    count = 1

    print("Qual o nível de dificuldade?")
    print(" 1) Fácil")
    print(" 2) Médio")
    print(" 3) Difícil",end="\n\n")

    nivel = int(input("Defina o nível: "))

    if( nivel == 1):
        tentativas = 20
    elif( nivel == 2 ):
        tentativas = 10
    else:
        tentativas = 5


    while (count <= tentativas) :
        print("*********************************")
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

            pontos_perdidos =  abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("\n")
    print("*********************************")
    print("Fim do Jogo, o número secreto era: {}".format(numero_secreto))
    print("Sua pontuação: {}".format(pontos))

if( __name__ == '__main__') :
    jogar()