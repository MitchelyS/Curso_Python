class Criptografia: 
    def __init__(self, frase):
        self.frase =frase.upper() # deixa tudo maiúsculo para padronizar
        self.mapa_vogais = {'A': '4', 'E': '3', 'I': '1', 'O': '0', 'U': '8'}

    def criptografar(self):
        resultado = ''
        for letra in  self.frase:
            if letra in self.mapa_vogais:
                esultado += self.mapa_vogais[letra]
            else:
                resultado += letra
        return resultado


# Programa principal
frase_usuario = input("Digite uma frase para criptografar: ")
cript = Criptografia(frase_usuario)
print("Frase criptografada:", cript.criptografar())