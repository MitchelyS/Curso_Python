#Orientação e Objeto
class Funcionario:
    def __init__(self, nome, salarioBase):#__init__ é o construtor que recebe nome e salário base
        self.nome = nome #atributos 
        self.salarioBase = salarioBase #atributos 

    def calcularSalario(self):#calcularSalario() retorna apenas o salário base
        return self.salarioBase
    
    def exibirDados(self):#exibirDados() mostra as informações formatadas #Def - definir 
        print(f"Nome:{self.nome}")
        print(f"Salário: R$ {self.calcularSalario():.2f}")

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, salarioBase, comissao):
        super().__init__(nome, salarioBase)
        self.comissao = comissao
    
    def calcularSalario(self):
        return self.salarioBase + self.comissao
    
    def exibirDados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário Base: R$ {self.salarioBase:.2f}")
        print(f"Comissão: R$ {self.comissao:.2f}")
        print(f"Salário Total: R$ {self.calcularSalario():.2f}")

class Funcionario:
    def __init__(self, nome, salarioBase):
        self.nome = nome
        self.salarioBase = salarioBase
    
    def calcularSalario(self):
        return self.salarioBase
    
    def exibirDados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.calcularSalario():.2f}")

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, salarioBase, comissao):
        super().__init__(nome, salarioBase)
        self.comissao = comissao
    
    def calcularSalario(self):
        return self.salarioBase + self.comissao
    
    def exibirDados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário Base: R$ {self.salarioBase:.2f}")
        print(f"Comissão: R$ {self.comissao:.2f}")
        print(f"Salário Total: R$ {self.calcularSalario():.2f}")

# Testando o programa
print("=== Sistema de Funcionários ===\n")

# Funcionário comum
funcionario1 = Funcionario("João Silva", 2500.00)
funcionario1.exibirDados()
print()

# Funcionário comissionado
funcionario2 = FuncionarioComissionado("Maria Santos", 2000.00, 1500.00)
funcionario2.exibirDados()

