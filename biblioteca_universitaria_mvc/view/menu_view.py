class MenuPrincipalView:

    @staticmethod
    def mostrar_menu():
        print("\n===== SISTEMA DE BIBLIOTECA =====\n")
        print("1 - Gerenciar Autores")
        print("2 - Gerenciar Livros")
        print("0 - Sair")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("\nEntrada inválida! Digite um número.\n")
            return -1