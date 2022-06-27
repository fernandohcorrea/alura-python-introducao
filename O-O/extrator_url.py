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
        if not self.url:
            raise ValueError('A url está invalida')

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


extrator_url = EstratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
valor_quetidade = extrator_url.get_valor_parametro("quantidade");
print(valor_quetidade)