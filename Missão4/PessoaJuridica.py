from Missão4.pessoa import pessoa

class PessoaJuridica(pessoa):
    def __init__(self, nome, numeroConta, dataAberturaConta, status, dataAberturaEmpresa, cnpj):
        super().__init__(nome, numeroConta, dataAberturaConta, status)
        self.__dataAberturaEmpresa = dataAberturaEmpresa
        self.__cnpj = cnpj

    # Getter e Setter para o atributo dataAberturaEmpresa
    @property
    def dataAberturaEmpresa(self):
        return self.__dataAberturaEmpresa

    @dataAberturaEmpresa.setter
    def dataAberturaEmpresa(self, dataAberturaEmpresa):
        self.__dataAberturaEmpresa = dataAberturaEmpresa

    # Getter e Setter para o atributo cnpj
    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        if len(cnpj) != 18:
            raise ValueError("O CNPJ deve conter 18 caracteres (no formato 00.000.000/0001-00).")
        self.__cnpj = cnpj
