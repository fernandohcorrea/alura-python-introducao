import re

endereco = "Rua Guanhães, 60, APTO 32, São Paulo, SP, 03140-030"

ereg = re.compile("[0-9]{5}[-]?[0-9]{3}")

busca = ereg.search(endereco);
cep = ""

if busca :
    cep = busca.group()

print(cep)