# Classe Alarme com 3 funções, sendo um atributo e 2 métodos.
class Alarme:

    # atributo que contém o 'estado' o alarme, podendo estar ativado (True) ou desativado (False)
    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    # Neste método temos o get, que irá retornar um valor booleano. Assim que eu coloco a classe em uma variável, posso escolher.
    def get_estado(self) -> bool:
        # O valor retornado é privado, não consigo chamar esse return diretamente com um objeto.
        return self.__estado
    
    # Neste método temos o set, que me torna possível alterar o estado da classe.
    def set_estado(self, valor: bool) -> None:
        # O isinstance está verificando se o valor é realmente um booleano e só irá alterar o valor do parâmetro valor caso seja.
        if isinstance(valor, bool):
            # Alterando o self.__estado (privado) para o 'valor' (booleano)
            self.__estado = valor

# Variável al recebendo a classe Alarme com o parâmetro False.
al = Alarme(False)
# Pritando o valor recebido com o método get_estado()
print(al.get_estado())
# Alterando o valor de estado para True com o set_estado(True)
al.set_estado(True)
# Pritando o get_estado() já com o valor alterado para True
print(al.get_estado())
