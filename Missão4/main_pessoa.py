from Missão4.pessoa import pessoa
from Missão4.PessoaFisica import PessoaFisica
from Missão4.PessoaJuridica import PessoaJuridica

# Instância da classe Pessoa
pessoa = pessoa("João", "123456", "2024-08-01", True)
print("Atributos da instância da classe Pessoa:")
pessoa.imprimir_atributos()

# Instância da classe PessoaFisica
pessoa_fisica = PessoaFisica("Ana", "789012", "2024-08-01", True, "1990-01-01", "123.456.789-00", "12345678")
print("\nAtributos da instância da classe PessoaFisica:")
pessoa_fisica.imprimir_atributos()

# Instância da classe PessoaJuridica
pessoa_juridica = PessoaJuridica("Empresa X", "345678", "2024-08-01", True, "2024-08-01", "12.345.678/0001-95")
print("\nAtributos da instância da classe PessoaJuridica:")
pessoa_juridica.imprimir_atributos()

# Alterações e validação
try:
    pessoa.cpf = "123.456.789-0"  # Deve gerar erro
except ValueError as e:
    print(f"\nErro ao definir CPF: {e}")

try:
    pessoa_juridica.cnpj = "12.345.678/0001-9"  # Deve gerar erro
except ValueError as e:
    print(f"\nErro ao definir CNPJ: {e}")

# Correção dos valores
pessoa_fisica.cpf = "123.456.789-00"
pessoa_juridica.cnpj = "12.345.678/0001-95"
