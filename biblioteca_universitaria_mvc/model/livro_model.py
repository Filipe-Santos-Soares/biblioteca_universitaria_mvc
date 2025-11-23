from model.biblioteca_model import BibliotecaModel

class LivroModel(BibliotecaModel):

    def cadastrar(self, titulo, ano, id_autor):
        try:
            self.cursor.execute("insert into livro (titulo, ano_publicacao, id_autor) VALUES (%s, %s, %s)", (titulo, ano, id_autor))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"\nErro ao cadastrar livro: {e}\n")
            self.conn.rollback()
            return False

    def listar(self):
        try:
            self.cursor.execute("select l.id, l.titulo, l.ano_publicacao, a.nome as nome_autor, a.id from livro l inner join autor a on l.id_autor = a.id order by l.titulo")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"\nErro ao listar livros: {e}\n")
            self.conn.rollback()
            return []
        
    def buscar_id(self, id_livro):
        try:
            self.cursor.execute("select * from livro where id = %s", (id_livro,))
            return self.cursor.fetchone()
        
        except Exception as e:
            print(f"Erro ao buscar livro: {e}")
            return None    

    def atualizar(self, id_livro, titulo, ano, id_autor):
        try:
            if not self.existe_id("livro", id_livro):
                return False
            
            self.cursor.execute("update livro set titulo=%s, ano_publicacao=%s, id_autor=%s where id=%s", (titulo, ano, id_autor, id_livro))
            self.conn.commit()
            return True
        
        except Exception as e:
            print(f"\nErro ao atualizar livro: {e}\n")
            self.conn.rollback()
            return False

    def excluir(self, id_livro):
        try:
            if not self.existe_id("livro", id_livro):                
                return False
            
            self.cursor.execute("delete from livro where id=%s", (id_livro,))
            self.conn.commit()
            return True
        
        except Exception as e:
            print(f"\nErro ao excluir livro: {e}\n")
            self.conn.rollback()

            return False
