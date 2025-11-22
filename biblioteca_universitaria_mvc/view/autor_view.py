class AutorView:

    @staticmethod
    def menu():
        print("\n=====Gerenciar Autores=====\n")
        print("1 - Cadastrar autor")
        print("2 - Listar autores")
        print("3 - Atualizar autor")
        print("4 - Excluir autor")
        print("0 - Voltar ao menu principal\n")

        try:
            return int(input("\nEscolha uma opção: "))
        except ValueError:
            print("\nEntrada inválida. Digite um número.\n")
            return -1

    
    @staticmethod
    def cadastrar():
        nome = input("Nome do autor: ")
        nacionalidade = input("Nacionalidade: ")
        return nome, nacionalidade
            
    @staticmethod
    def listar(autores):
        if not autores:
            print("\nNenhum autor cadastrado.\n")
        else:
            print("\n=====Lista de Autores=====\n")
            for p in autores:
                print(f"ID: {p[0]} | Nome: {p[1]} | Nacionalidade: {p[2]}") 

    @staticmethod
    def id_atualizar():
        try:
            return int(input("ID do autor a atualizar: "))
        except ValueError:
            print("\nEntrada inválida.\n")
            return None

    @staticmethod
    def novos_dados():
        nome = input("\nNovo nome: ")
        nacionalidade = input("Nova nacionalidade: ")
        return nome, nacionalidade
        
    @staticmethod
    def excluir():
        try:
            id_autor = int(input("\nID do autor a ser excluído: "))
            return id_autor
        except ValueError:
            print("\nEntrada inválida.\n")
            return None
    
    @staticmethod
    def mensagem(msg):
        print(msg)