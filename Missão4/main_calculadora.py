from Calculadora import Calculadora

# Instância da classe Calculadora
calc = Calculadora(10, 5, '+')

# Exibindo o resultado
calc.mostrarResultado()

# Testando outras operações
calc.valorA = 20
calc.valorB = 4
calc.operacao = '-'
calc.mostrarResultado()

calc.operacao = '*'
calc.mostrarResultado()

calc.operacao = '/'
calc.mostrarResultado()

# Testando divisão por zero
calc.valorB = 0
calc.mostrarResultado()  # Deve gerar erro
