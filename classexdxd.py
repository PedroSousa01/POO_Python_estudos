class Carro:

    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
meu_carro = Carro('Toyota', 'Corolla', 2020)

print(f'Modelo: {meu_carro.modelo}')
print(f'Marca: {meu_carro.marca}')
print(f'Ano: {meu_carro.ano}')
