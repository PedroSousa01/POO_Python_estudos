# Aula 11 explicando sobre associação de dependência, no qual uma classe é dependente da existência de outra.
# No caso abaixo, a classe Pessoa para funcionar necessita dos métodos presentes na classe Casa, logo, é uma associação de dependência.
from typing import Type # Biblioteca que permite transformar uma classe em um tipo, para mostrar na classe dependente.

class Casa: # Classe Casa, com 1 método construtor e 2 métodos próprios.
    def __init__(self) -> None:
        self.__endereco = 'Rua Jerusalém'
    
    def acender_luzes(self) -> None:
        print('Estou Acendendo as Luzes!')
    
    def get_endereco(self) -> str:
        return self.__endereco
    
class Pessoa: # Classe Pessoa dependente da classe Casa para funcionar, já que utiliza os métodos .acender_luzes() e .get_endereco()
    def __init__(self, nome: str, local: Type[Casa]) -> None: # Usei o Type para transformar Casa em um tipo e poder mostrar os métodos.
        self.__local = local
        self.__nome = nome
    
    def entrar_no_local(self) -> None:
        self.__local.acender_luzes()
    
    def apresentar_local(self) -> None:
        endereco = self.__local.get_endereco()
        print(endereco)

casa_de_amigo = Casa()
ana = Pessoa('Ana', casa_de_amigo)
ana.entrar_no_local()
ana.apresentar_local()
