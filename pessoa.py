class Pessoa:
    def __init__(self, nome, numeroConta, dataAberturaConta, status):
        self.__nome = nome
        self.__numeroConta = numeroConta
        self.__dataAberturaConta = dataAberturaConta
        self.__status = status

    # Getter e Setter para o atributo nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # Getter e Setter para o atributo numeroConta
    @property
    def numeroConta(self):
        return self.__numeroConta

    @numeroConta.setter
    def numeroConta(self, numeroConta):
        self.__numeroConta = numeroConta

    # Getter e Setter para o atributo dataAberturaConta
    @property
    def dataAberturaConta(self):
        return self.__dataAberturaConta

    @dataAberturaConta.setter
    def dataAberturaConta(self, dataAberturaConta):
        self.__dataAberturaConta = dataAberturaConta

    # Getter e Setter para o atributo status
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    def imprimir_atributos(self):
        print(f"Nome: {self.__nome}")
        print(f"Número da Conta: {self.__numeroConta}")
        print(f"Data de Abertura da Conta: {self.__dataAberturaConta}")
        print(f"Status: {self.__status}")
