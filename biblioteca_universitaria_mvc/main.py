from view.menu_view import MenuPrincipalView
from controller.autor_controller import AutorController
from controller.livro_controller import LivroController


def main():
    autor_controller = AutorController()
    livro_controller = LivroController()

    while True:
        opcao = MenuPrincipalView.mostrar_menu()

        if opcao == 1:
            autor_controller.executar()

        elif opcao == 2:
            livro_controller.executar()

        elif opcao == 0:
            print("\nSaindo do sistema...\n")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()