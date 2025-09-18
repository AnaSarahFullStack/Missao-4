from Missão4.pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, numeroConta, dataAberturaConta, status, dataNascimento, cpf, rg):
        super().__init__(nome, numeroConta, dataAberturaConta, status)
        self.__dataNascimento = dataNascimento
        self.__cpf = cpf
        self.__rg = rg

    # Getter e Setter para o atributo dataNascimento
    @property
    def dataNascimento(self):
        return self.__dataNascimento

    @dataNascimento.setter
    def dataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento

    # Getter e Setter para o atributo cpf
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) != 14:
            raise ValueError("O CPF deve conter 14 caracteres (no formato 000.000.000-00).")
        self.__cpf = cpf

    # Getter e Setter para o atributo rg
    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, rg):
        self.__rg = rg
