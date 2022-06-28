

import re

import re

url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'

ereg = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')

match = ereg.match(url)

if not match :
    raise ValueError('A URL não é valida')

print(url)