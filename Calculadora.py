class Calculadora:
    def __init__(self, valorA=0.0, valorB=0.0, operacao='+'):
        self.__valorA = float(valorA)
        self.__valorB = float(valorB)
        self.__operacao = operacao.strip()

    # Getters e Setters
    @property
    def valorA(self):
        return self.__valorA

    @valorA.setter
    def valorA(self, valorA):
        self.__valorA = float(valorA)

    @property
    def valorB(self):
        return self.__valorB

    @valorB.setter
    def valorB(self, valorB):
        self.__valorB = float(valorB)

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao.strip()

    def validarOperacao(self, operacao=None):
        if operacao is None:
            operacao = self.__operacao
        operacoes_validas = ['+', '-', '*', '/']
        return operacao in operacoes_validas

    def calcular(self):
        if not self.validarOperacao():
            raise ValueError(f"Operação '{self.__operacao}' inválida!")

        if self.__operacao == '+':
            return self.__valorA + self.__valorB
        elif self.__operacao == '-':
            return self.__valorA - self.__valorB
        elif self.__operacao == '*':
            return self.__valorA * self.__valorB
        elif self.__operacao == '/':
            if self.__valorB == 0:
                raise ZeroDivisionError("Não é possível dividir por zero!")
            return self.__valorA / self.__valorB

    def mostrarResultado(self):
        try:
            resultado = self.calcular()
        except Exception as e:
            print("Erro:", e)
        else:
            print(f"{self.__valorA} {self.__operacao} {self.__valorB} = {resultado}")

    def entradaDados(self):
        while True:
            try:
                a = input("Digite o valor A: ").strip()
                b = input("Digite o valor B: ").strip()
                op = input("Digite a operação (+, -, *, /): ").strip()
                # tenta converter para float — se falhar, vai pro except
                self.__valorA = float(a)
                self.__valorB = float(b)
                if not self.validarOperacao(op):
                    print("Operação inválida. Use apenas: + - * /")
                    continue
                self.__operacao = op
            except ValueError:
                print("Entrada inválida. Por favor, digite números válidos.")
                continue
            break


if __name__ == "__main__":
    calc = Calculadora()
    while True:
        calc.entradaDados()
        calc.mostrarResultado()
        again = input("Deseja calcular novamente? (s/n): ").strip().lower()
        if again not in ('s', 'sim', 'y', 'yes'):
            print("Encerrando calculadora. Até mais!")
            break
