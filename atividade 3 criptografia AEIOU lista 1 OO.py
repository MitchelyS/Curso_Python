# A → 4  
# E → 3  
# I → 1  
# O → 0  
# U → 8  
#CLASSE
class Criptografia:
    def __init__(self, frase): #METODO CONSTRUTOR
        self.frase = frase     #ATRIBUTOS
# CRIANDO A CRIPTOGRAFIA   
    def criptografar(self): #METODO CONSTRUTOR
        tabela = {
            "A": "4", "a": "4",
            "E": "3", "e": "3",
            "I": "1", "i": "1",
            "O": "0", "o": "0",
            "U": "8", "u": "8"

        }
# CRIANDO O LOOP
        frase_final = ""
        for letra in self.frase:
            if letra in tabela:
               frase_final += tabela[letra]
            else:
                frase_final +=  letra
        return frase_final
    
# STRING PRO USUARIO 
frase_usuario = input("Digite uma frase: ")
cripto = Criptografia(frase_usuario)
print("Frase criptografada:", cripto.criptografar())