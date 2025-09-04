class Departamento:
 def __init__(self, nome):
  self.nome = nome
class Professor:
 def __init__(self, nome, departamento):
  self.nome = nome
 self.departamento = departamento 
 # Associação com
Departamento
def exibir_info(self):
  print(f"Professor: {self.nome}")
  print(f"Departamento: {self.departamento.nome}")
# Criando o departamento
  dep_comp = Departamento("Computação")
# Criando o professor associado ao departamento
  prof = Professor("Henrique", dep_comp)
# Exibindo informações 
  prof.exibir_info()