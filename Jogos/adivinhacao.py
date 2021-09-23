print("*********************************")
print("Bem vindo ao jogo de adivinhação")
print("*********************************")

numero_secreto = 55

chute = input("Digite um número: ")
chute = int(chute)

print("Você digito",":", chute)

if( chute == numero_secreto ):
    print("Você acertou")
else:
    print("Você errou")


print("Fim do Jogo")