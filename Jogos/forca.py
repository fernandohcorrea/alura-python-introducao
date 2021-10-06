
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de forca")
    print("*********************************")

    palavra_secreta = "queijo"

    enforcado = False
    acertou = False
    chute = ""

    while ( not enforcado and not acertou ):
        print("*********************************")
        chute = input("Digite uma letra: ")

        if (chute == 'q') :
            acertou = True




    print("\n")
    print("*********************************")
    print("Fim do Jogo")


if( __name__ == '__main__') :
    jogar()