import re
class EstratorURL:
    def __init__(self, url:str):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        ereg = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')

        match = ereg.match(self.url)

        if not match :
            raise ValueError('A URL não é válida')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        self.url_base = self.url[:indice_interrogacao]
        self.url_parametros = self.url[indice_interrogacao+1:]
        return self.url_base

    def get_url_parametros(self):
        self.get_url_base()
        return self.url_parametros

    def get_valor_parametro(self, parametro_busca):
        self.get_url_parametros()
        indice_parametro = self.url_parametros.find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.url_parametros.find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.url_parametros[indice_valor:]
        else:
            valor = self.url_parametros[indice_valor:indice_e_comercial]

        return valor

    def __len__(self) :
        return len(self.url)

    def __str__(self) :
        data = [
            "Url: " + self.url,
            "Url Base: " + self.get_url_base(),
            "Parâmetros: " + self.get_url_parametros()
        ]
        return "\n".join(data)

    def __eq__(self, __o: object) :
        return self.url == __o.url

url="bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

extrator_url = EstratorURL(url)
extrator_url2 = EstratorURL(url)
print("Comparando Objetos: ", extrator_url == extrator_url2 )


print("Tamanho da Url: ", len(extrator_url))
print(extrator_url)

valor_quatidade = extrator_url.get_valor_parametro("quantidade");

print(valor_quatidade)