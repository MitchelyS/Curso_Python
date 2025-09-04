# Entrada de dados
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota (0 a 10): "))
nota2 = float(input("Digite a segunda nota (0 a 10): "))

# Cálculo da média
media = (nota1 + nota2) / 2

# Verificação da situação Condição
if media >= 7:
    situacao = "Etudou né Parabens APROVADISSIMO"
elif media >= 5:
    situacao = "Meus PÊSAMES ta de Recuperação"
else:
    situacao = "ixi Reprovado"

# Saída dos resultados
print(f"\nAluno: {nome}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
