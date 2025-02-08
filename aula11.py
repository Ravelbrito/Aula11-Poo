class carro:
    def __init__(self, marca,ano,modelo):
        ...
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, aceleracao):
        self.velocidade += aceleracao

    def frear (self, desaceleracao):
        if self.velocidade ==0:
            print (f'{self.marca} {self.modelo} já parado')
        else:
            self.velocidade -= desaceleracao



meu_carro = carro('honda', 2025, 'Civic Type R')
meu_carro.acelerar(20)
print(meu_carro.velocidade)
meu_carro.frear(20)
meu_carro.frear(20)



# print(meu_carro.marca)
# print(meu_carro.ano)
# print(meu_carro.modelo)