import os
import random

def display_forca(step=0):
    print("*********************************")

    if (step == 0):
        print("Bem vindo ao jogo de forca".upper())
        print("   ______                 ")
        print("  |/     |                ")
        print("  |     (_)               ")
        print("  |    --|--              ")
        print("  |      |                ")
        print("  |     / \               ")
        print("  |                       ")
        print("  |                       ")
        print("--------------------------", end="\n\n")
        return

    print("   ______                 ")
    print("  |/     |                ")

    if (step == 1):
        print("  |     (_)               ")
        print("  |                       ")
        print("  |                       ")
        print("  |                       ")

    if (step == 2):
        print("  |     (_)               ")
        print("  |      |                ")
        print("  |      |                ")
        print("  |                       ")

    if (step == 3):
        print("  |     (_)               ")
        print("  |    --|                ")
        print("  |      |                ")
        print("  |                       ")

    if (step == 4):
        print("  |     (_)               ")
        print("  |    --|--              ")
        print("  |      |                ")
        print("  |                       ")

    if (step == 5):
        print("  |     (_)               ")
        print("  |    --|--              ")
        print("  |      |                ")
        print("  |     /                 ")

    if (step == 6) :
        print("  |     (_)               ")
        print("  |    --|--              ")
        print("  |      |                ")
        print("  |     / \               ")

    print("  |                       ")
    print("  |                       ")
    print("--------------------------", end="\n\n")

def display_morreu_enforcado():
    print("Puxa, você foi enforcado!")
    print("       _______________        ")
    print("      /               \       ")
    print("     /                 \      ")
    print("  /\/                   \/\   ")
    print("  \ |   X X       X X   | /   ")
    print("   \|    X         X    |/    ")
    print("    |   X X       X X   |     ")
    print("    |                   |     ")
    print("    \__       X       __/     ")
    print("      |\     X X     /|       ")
    print("      | |           | |       ")
    print("      | I I I I I I I |       ")
    print("      |  I I I I I I  |       ")
    print("      \_             _/       ")
    print("        \_         _/         ")
    print("          \_______/           ")

def display_venceu_a_forca():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def obter_palavra():
    palavras_list = []
    palavras_path = os.path.dirname(os.path.abspath(__file__))
    palavras_path = palavras_path + "/palavras.txt"

    with open(palavras_path) as arquivo:
        for palavra in arquivo:
            palavras_list.append(palavra.strip().upper())

    idx = random.randrange(0,len(palavras_list)-1)

    palavra_secreta = palavras_list[idx]
    return palavra_secreta

def obter_chute():
    chute = str(input("Digite uma letra: "))
    return chute.strip().upper()

def busca_letras(chute, palavra_secreta, letras_acertadas):
    idx = 0
    for letra in palavra_secreta :
        if(chute == letra) :
            print("Encontrei a letra '{}' na posição: {}".format(chute, (idx+1)))
            letras_acertadas[idx] = chute
        idx += 1

def jogar():

    display_forca(0)
    palavra_secreta = obter_palavra()
    letras_acertadas = ["_" for l in palavra_secreta]

    enforcado = False
    acertou = False
    num_enforcar = 6
    erros = 0
    chute = ""

    print(letras_acertadas)

    while ( not enforcado and not acertou ):
        chute = obter_chute()

        if ( len(chute) > 1 ) :
            print("*********************************")
            print("Digite apenas uma letra")
            continue

        if(chute in palavra_secreta) :
            busca_letras(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            display_forca(erros)
            print("Não encontrei a letra '{}'. Você tem '{}' entativas".format(chute, (num_enforcar - erros)))

        print("*********************************")
        print(letras_acertadas)

        if ('_' not in  letras_acertadas and erros < num_enforcar) :
            acertou = True
            break

        if( erros >= num_enforcar ) :
            enforcado = True
            break


    print("\n")
    print("***********************************************")
    print("Palavra Secreta '{}'.".format(palavra_secreta))
    print("***********************************************")

    if(enforcado == True) :
        display_morreu_enforcado()
    else :
        display_venceu_a_forca()


if( __name__ == '__main__') :
    jogar()