# Classe 'Calculadora' que efetua a operação de subtrair ou adicionar.
class Calculadora:
    
    # Função calcular (pública), que irá retornar os valores baseado em 3 parâmetros: op (operador + ou -);
    # num1 e num2 que irá ser informado pelo usuário quando requisitar a classe e a função.
    def calcular(self, op, num1, num2):
        if op == '+':
            # Caso parâmetro op seja '+' irá retornar o valor da função __adicionar (privada) de num1 e num2
            return self.__adicionar(num1, num2)
        elif op == '-':
            # Caso parâmetro op seja '-' irá retornar o valor da função __subtrair (privada) de num1 e num2
            return self.__subtrair(num1, num2)
        else:
            # Caso parâmetro op seja diferente de '+' e '-' irá retornar uma mensagem de erro.
            print('Operação Inválida.')
        
    # função __adicionar (privada) que só pode ser acessada no contexto da classe, não pelo objeto.
    def __adicionar(self, num1, num2):
        return num1 + num2
    # função __subtrair (privada) que também só pode ser requisitada dentro do contexto da classe Calculadora.
    def __subtrair(self, num1, num2):
        return num1 - num2

# variável calculadora recebe a classe Calculadora()
calculadora = Calculadora()
# Variável resultado recebendo a função calcular e os seus parâmetros que está dentro da calculadora (linha acima)
resultado = calculadora.calcular('+', 3, 2)
# Printando o resultado da soma de 3 + 2 que é 5
print(resultado)

# Anotações: Para tornar um atributo ou método privado, ou seja, os objetos de contexto externo à classe, não poderá acessar diretamente, necessita
# apenas que coloque dois underlines após o ponto (ex: self.__adicionar).
# Fazer isso é muito útil a longo prazo, já que facilita e muito a refatoração do código, já que fica bem explicito onde ficaria um possível erro.
