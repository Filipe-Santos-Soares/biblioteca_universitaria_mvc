from model.livro_model import LivroModel
from view.livro_view import LivroView

class LivroController:
    def __init__(self):
        self.model = LivroModel()
        self.view = LivroView()

    def executar(self):
        while True:
            opcao = self.view.menu()

            if opcao == 1:
                titulo, ano, id_autor = self.view.cadastrar()
                if not titulo or not ano or not id_autor:
                    self.view.mensagem("\nTItulo, ano de publicação e o ID do autor não podem ser vazios.\n")
                    continue

                if self.model.cadastrar(titulo, ano, id_autor):
                    self.view.mensagem("\nLivro cadastrado com sucesso!\n")
                else:
                    self.view.mensagem("\nErro ao cadastrar livro.\n")

            elif opcao == 2:
                livros = self.model.listar()
                self.view.listar(livros)

            elif opcao == 3:
                id_livro = self.view.id_atualizar()
                if not id_livro:
                    continue

                livro = self.model.buscar_id(id_livro)
                if not livro:
                    self.view.mensagem("\nErro: livro não encontrado.\n")
                    continue

                titulo, ano, id_autor = self.view.novos_dados()
                if self.model.atualizar(id_livro, titulo, ano, id_autor):
                    self.view.mensagem("\nLivro atualizado com sucesso!\n")
                else:
                    self.view.mensagem("\nErro ao atualizar livro.\n")

            elif opcao == 4:
                id_livro = self.view.excluir()
                if not id_livro:
                    continue
                if self.model.excluir(id_livro):
                    self.view.mensagem("\nLivro excluído com sucesso!\n")
                else:
                    self.view.mensagem("\nErro ao excluir livro: ID não encontrado.\n")

            elif opcao == 0:
                self.view.mensagem("\nVoltando ao menu principal...\n")
                break

            else:
                self.view.mensagem("\nOpção inválida!\n")