
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de forca")
    print("*********************************")

    palavra_secreta = "banana"

    enforcado = False
    acertou = False
    chute = ""

    while ( not enforcado and not acertou ):
        print("*********************************")
        chute = str(input("Digite uma letra: "))
        chute = chute.strip()
        chute = chute.upper()

        if ( len(chute) > 1 ) :
            print("Digite apenas uma letra")
            continue

        achou = False
        idx = 0

        for letra in palavra_secreta :
            if(chute == letra.upper()) :
                print("Encontrei a letra {} na posição {}".format(letra, idx))
            idx = idx + 1



    print("\n")
    print("*********************************")
    print("Fim do Jogo")


if( __name__ == '__main__') :
    jogar()