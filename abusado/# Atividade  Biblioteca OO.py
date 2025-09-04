# Autor → guarda nome e nacionalidade.
# Livro → guarda título, ano e referência ao Autor (agregação).
# Biblioteca → guarda nome e livros criados internamente (composição).
# Usuario → guarda nome, sabe a qual Biblioteca pertence (associação) e pode pegar livros emprestados (dependência).

#---------------------------AUTOR----------------------------
class Autor:
    def __init__(self, nome, nacionalidade): # DEF → definir 
# init → é um método especial (um construtor) que é chamado automaticamente quando um novo objeto de uma classe é criado.
        self.nome = nome # atributo: nome do autor
        self.nacionalidade = nacionalidade # atributo: nacionalidade do autor

#----------------------------Livro---------------------------
class Livro:
    def __init__(self, titulo, ano, autor): #Objetos Ex: nome, titulo e nome 
        self.titulo = titulo #
        self.ano = ano 
        self.autor = autor


#----------------------------Biblioteca------------------------
class Biblioteca:
    def __init__(self, nome): #
        self.nome = nome # nome da biblioteca
        self.livros = [] # lista para guardar os livros criados dentro dela
    
    def adicionar_livro(self,titulo, ano, autor):
 # Aqui a biblioteca cria o livro internamente
        livro =Livro(titulo, ano, autor)
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros: #Esse for vai percorrer cada livro dessa lista, um por vez. A cada volta do loop, a variável livro vai conter um objeto da classe Livro
         print(f"{livro.titulo} ({livro.ano}) - Autor: {livro.autor.nome}") 

#----------------------------USUARIO------------------------
class Usuario:
    def __init__(self, nome, biblioteca):
        self.nome = nome
        self.biblioteca = biblioteca  # associação: usuário sabe qual biblioteca usa

    def pegar_livro_emprestado(self, titulo):
        # dependência: usa um livro temporariamente
        for livro in self.biblioteca.livros:
            if livro.titulo == titulo:
                print(f"{self.nome} pegou emprestado o livro '{livro.titulo}' do autor {livro.autor.nome}")
                return
            
        print(f"Livro '{titulo}' não encontrado na biblioteca.")

    
"""Começando o Laço de repetição necessariamente tem que usar o break, tudo está contido nesse laço"""

autores = []
usuarios = []
biblioteca = Biblioteca("Biblioteca Central")

while True: #LAÇO
    print("\n=== MENU ===")
    print("1 - Cadastrar Autor")
    print("2 - Adicionar Livro")
    print("3 - Listar Livro")
    print("4 - Cadastrar Ususario")
    print("5 - Pegar livro Emprestado")
    print("0 - Sair")

    opcao = input("Escolha: ") # == → igual 
                               # O operador = é o operador de atribuição.

#================input()→ função sempre retorna os dados inseridos como uma string===========
    if opcao == "1":
        nome = input("Nome do Autor: ")
        nacionalidade = input("Nacionalidade")
        autores.append(Autor(nome, nacionalidade))
        print("Autor Cadastrado com sucesso! ;)")
   
    elif opcao == "2":
        if not autores:
            print("cadastre um autor primeiro!")
            continue
        titulo = input("Titulo do livro: ")
        ano = int(input("Ano: "))
        print("\nEscolha o autor:")
        for i, autor in enumerate(autores): #loop enquanto i= contador 
            print(f"{i+1}. {autor .nome}({autor.nacionalidade})")
        escolha = int(input("Numero do autor")) -1
        Biblioteca.adicionar_livro(titulo, ano, autores[escolha])
        print("livro adiconado com sucesso!")
   
    elif opcao == "3":
        biblioteca.listar_livros()

    elif opcao =="4":
        nome = input("Nome do usuário:")
        usuarios.append(Usuario(nome, biblioteca))
        print("Usário cadastrado com sucesso!")

    elif opcao =="5":
        if not usuarios:
            print("Cadastre um usuário porfavor! ")
            continue
        nome_usuario = input("Nome do usuário:")
        usuario = next((u for u in usuarios if u.nome == nome_usuario), None)
        if usuario:
            titulo = input("Titulo do livro:")
            usuario.pegar_livro_emprestado(titulo)
        else:
            print("Usuario não encontrado.")

    elif opcao == "0":
        break

    else:
        print("opção inválida!")