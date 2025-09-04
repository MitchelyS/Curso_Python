#LISTA DE CARRINHO 
class Produto:
    #METODOS CONSTRUTOR
    def __init__(self, nome, preco, quantidade):
        #ATRIBUTOS 
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
#Os getters e setters estão acessando atributos privados (self.__nome, self.__preco, self.__quantidade).

    # Getters (ler valores)
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade    
    
    # Setters (alterar valores)
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_preco(self, novo_preco):
        if novo_preco >= 0:       # proteção para não colocar preço negativo
            self.__preco = novo_preco

    def set_quantidade(self, nova_quantidade):
        if nova_quantidade >= 0:  # proteção para não colocar quantidade negativa
            self.__quantidade = nova_quantidade

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []  # lista de produtos

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, nome):
        for p in self.produtos:
            if p.get_nome() == nome:
                self.produtos.remove(p)
                return True   # removido com sucesso
        return False          # não encontrou produto

    def calcular_total(self):
        total = 0
        for p in self.produtos:
            total += p.get_preco() * p.get_quantidade()
        return total

    def listar_produtos(self):
        if not self.produtos:
            print("O carrinho está vazio.")
        for p in self.produtos:
            print(f"{p.get_nome()} - Preço: R${p.get_preco():.2f} - Quantidade: {p.get_quantidade()}")

        #MENU
        