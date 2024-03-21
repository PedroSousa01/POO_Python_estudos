from typing import Type
 
class Animal:

    def comer(self) -> None:
        print('O animal está comendo...')
    
    def dormir(self) -> None:
        print('O naimal está dormindo...')
    
    def andar(self) -> None: 
        print('O animal está andando na jaula...')

class Aves(Animal):

    def __init__(self):
        super().__init__()
    
    def cantar(self) -> None:
        print('A ave está cantando...')
    
class Pinguim(Aves):

    def __init__(self):
        super().__init__()

    def escorregar(self) -> None:
        print('O Pinguim está escorregando no gelo...')
    
class Pessoa:

    def observar(self, animal: Type[Animal]):
        animal.comer(self)

pedro = Pessoa()
pinguim = Animal()
pedro.observar(Pinguim)
