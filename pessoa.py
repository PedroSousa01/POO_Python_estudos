# Padrão a ser seguido para organização de classes e funções.

class Pessoa:  # Substantivo

    def __init(self, name: str, idade: int) -> None: 
        self.name = name    # Substantivo
        self.idade = idade  # Substantivo
    
    def dirigir(self, veiculo: str) -> None:  # Verbos
        print(f'Dirigindo um(a) {veiculo}.')
    
    def cantar(self) -> None:            #Verbos
        print('Lalalalalala...')
    
    def apresentar_idade(self) -> int:  # Verbos
        return self.idade

