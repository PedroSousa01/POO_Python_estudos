class Mae:
    def __init__(self, endereco: str) -> None:
        self.endereco = endereco
        self.sobrenome = 'Silva'
    
    def comer(self) -> None:
        print('Estou comendo...')
    
    def estudar(self) -> None:
        print('Estou estudando...')

class Filha (Mae):
    def __init__(self, endereco: str) -> None:
        super().__init__(endereco)
    
    def brincar(self, brinquedo: str) -> None:
        print(f'Estou brincando com {brinquedo}!')

class Neta (Filha):
    def __init__(self, endereco: str) -> None:
        super().__init__(endereco)

ana = Mae('Rua Elvira')
clara = Filha('Rua do Bolo')
maria = Neta('Rua das Árvores')
print(maria.endereco)
clara.brincar('boneca')
maria.brincar('bola')
