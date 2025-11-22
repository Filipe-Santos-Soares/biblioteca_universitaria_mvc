from model.autor_model import AutorModel
from view.autor_view import AutorView

class AutorController:
    def __init__(self):
        self.model = AutorModel()
        self.view = AutorView()

    def executar(self):
        while True:
            opcao = self.view.menu()

            if opcao == 1:
                nome, nacionalidade = self.view.cadastrar()
                if not nome or not nacionalidade:
                    self.view.mensagem("\nNome e nacionalidade não podem ser vazios.\n")
                    continue

                if self.model.cadastrar(nome, nacionalidade):
                    self.view.mensagem("\nAutor cadastrado com sucesso!\n")
                else:
                    self.view.mensagem("\nErro ao cadastrar autor.\n")

            elif opcao == 2:
                autores = self.model.listar()
                self.view.listar(autores)

            elif opcao == 3:
                id_autor = self.view.id_atualizar()
                if not id_autor:
                    continue

                autor = self.model.buscar_id(id_autor)
                if not autor:
                    self.view.mensagem("\nErro: autor não encontrado.\n")
                    continue

                nome, nacionalidade = self.view.novos_dados()
                if self.model.atualizar(id_autor, nome, nacionalidade):
                    self.view.mensagem("\nAutor atualizado com sucesso!\n")
                else:
                    self.view.mensagem("\nErro ao atualizar autor.\n")

            elif opcao == 4:
                id_autor = self.view.excluir()
                if not id_autor:
                    continue
                if self.model.excluir(id_autor):
                    self.view.mensagem("\nAutor excluído com sucesso!\n")
                else:
                    self.view.mensagem("\nErro ao excluir autor: ID não encontrado.\n")

            elif opcao == 0:
                self.view.mensagem("\nVoltando ao menu principal...\n")
                break

            else:
                self.view.mensagem("\nOpção inválida!\n")