class LivroView:

    @staticmethod
    def menu():
        print("\n=====Gerenciar Livros=====\n")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Atualizar livro")
        print("4 - Excluir livro")
        print("0 - Voltar ao menu principal\n")

        try:
            return int(input("\nEscolha uma opção: "))
        except ValueError:
            print("\nEntrada inválida. Digite um número.\n")
            return -1

    
    @staticmethod
    def cadastrar():
        titulo = input("Titulo do livro: ")
        ano = int(input("Ano de publicação: "))
        id_autor = int(input("Id do autor: "))
        return titulo, ano, id_autor
            
    @staticmethod
    def listar(livros):
        if not livros:
            print("\nNenhum livro cadastrado.\n")
        else:
            print("\n=====Lista de Livros=====\n")
            for l in livros:
                print(f"ID: {l[0]} | Titulo: {l[1]} | Ano de Publicação: {l[2]} | Autor: {l[3]}") 

    @staticmethod
    def id_atualizar():
        try:
            return int(input("ID do livro a atualizar: "))
        except ValueError:
            print("\nEntrada inválida.\n")
            return None

    @staticmethod
    def novos_dados():
        titulo = input("\nNovo titulo: ")
        ano = input("Nova ano de publicação: ")
        id_autor = input("ID do autor: ")
        return titulo, ano, id_autor
        
    @staticmethod
    def excluir():
        try:
            id_livro = int(input("\nID do livro a ser excluído: "))
            return id_livro
        except ValueError:
            print("\nEntrada inválida.\n")
            return None
    
    @staticmethod
    def mensagem(msg):

        print(msg)
