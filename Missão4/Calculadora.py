class Calculadora:
    def __init__(self, valorA=0, valorB=0, operacao='+'):
        self.__valorA = valorA
        self.__valorB = valorB
        self.__operacao = operacao

    # Getters e Setters
    @property
    def valorA(self):
        return self.__valorA

    @valorA.setter
    def valorA(self, valorA):
        self.__valorA = valorA

    @property
    def valorB(self):
        return self.__valorB

    @valorB.setter
    def valorB(self, valorB):
        self.__valorB = valorB

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao

    def validarOperacao(self, operacao):
        operacoes_validas = ['+', '-', '*', '/']
        return operacao in operacoes_validas

    def calcular(self):
        if not self.validarOperacao(self.__operacao):
            print(f"Operação '{self.__operacao}' inválida!")
            exit()

        if self.__operacao == '+':
            return self.__valorA + self.__valorB
        elif self.__operacao == '-':
            return self.__valorA - self.__valorB
        elif self.__operacao == '*':
            return self.__valorA * self.__valorB
        elif self.__operacao == '/':
            if self.__valorB == 0:
                print("Não é possível dividir por zero!")
                exit()
            return self.__valorA / self.__valorB

    def mostrarResultado(self):
        print(f"{self.__valorA} {self.__operacao} {self.__valorB} = {self.calcular()}")

class Calculadora:
    # (mantém o código existente)

    def entradaDados(self):
        try:
            self.__valorA = float(input("Digite o valor A: "))
            self.__valorB = float(input("Digite o valor B: "))
            self.__operacao = input("Digite a operação (+, -, *, /): ")
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")
            exit()
