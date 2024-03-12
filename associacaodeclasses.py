class Interruptor:

    def __init__(self, comodo: str) -> None:
        self.__comodo = comodo
    
    def acender(self) -> None:
        print(f'Acendendo a luz do(a) {self.__comodo}!')
    
    def apagar(self) -> None:
        print(f'Apagando a luz do(a) {self.__comodo}!')

class Pessoa:

    def acender_luzes(self, interruptor: Interruptor) -> None:
        interruptor.acender()

    def apagar_luzes(self, interruptor: Interruptor) -> None:
        interruptor.apagar()
    
    def dormir(self) -> None:
        print('Fui dormir...')


pedro = Pessoa()
interruptor_quarto = Interruptor('Quarto')
interruptor_sala = Interruptor('Sala')

interruptor_quarto.acender()
pedro.acender_luzes(interruptor_quarto)
pedro.apagar_luzes(interruptor_sala)
pedro.dormir()
