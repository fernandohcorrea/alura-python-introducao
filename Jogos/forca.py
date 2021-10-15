
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de forca")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ['_','_','_','_','_','_',]

    enforcado = False
    acertou = False
    chute = ""

    while ( not enforcado and not acertou ):
        print(letras_acertadas)
        print("*********************************")
        chute = str(input("Digite uma letra: "))
        chute = chute.strip()
        chute = chute.upper()

        if ( len(chute) > 1 ) :
            print("Digite apenas uma letra")
            continue

        idx = 0
        for letra in palavra_secreta :
            if(chute == letra.upper()) :
                print("Encontrei a letra '{}' na posição: {}".format(chute, (idx+1)))
                letras_acertadas[idx] = chute
            idx = idx + 1


        if ('_' not in  letras_acertadas) :
            print(letras_acertadas)
            break



    print("\n")
    print("*********************************")
    print("Fim do Jogo")


if( __name__ == '__main__') :
    jogar()