#CONTADOR DE VOGAIS 
palavra = input("Digite uma palavra: ")
contador = 0
for letra in palavra:# é a estrutura de repetição, ou loop, usada para iterar sobre uma sequência de itens, como uma lista, tupla ou string 
    if letra in "aeiou":
        contador += 1
print(f"A palavra '{palavra}' tem {contador} vogais.")
palavra = input("Digite uma palavra: ").lower()
contador = 0

for letra in palavra:
    if letra in "aeiou":
        contador += 1

print(f"A palavra '{palavra}' tem {contador} vogais.")

