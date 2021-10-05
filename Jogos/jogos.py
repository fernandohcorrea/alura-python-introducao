import adivinhacao
import forca

def jogos():
    print("*********************************")
    print("       Escolha seu jogo!         ")
    print("*********************************",end="\n\n")

    opcao = 0

    print(" 1) Adivinhação númerica")
    print(" 2) Forca")

    opcao = int(input("Qual Jogo: "))


    if ( opcao == 1 ) :
        adivinhacao.jogar()
    elif( opcao == 2 ) :
        forca.jogar()
    else :
        print('Tchau, Tchau!')

if( __name__ == '__main__'):
    jogos()