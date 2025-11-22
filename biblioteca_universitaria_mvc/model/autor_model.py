from model.biblioteca_model import BibliotecaModel

class AutorModel(BibliotecaModel):

    def cadastrar(self, nome, nacionalidade):
        try:
            self.cursor.execute("insert into autor (nome, nacionalidade) VALUES (%s, %s)", (nome, nacionalidade))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"\nErro ao cadastrar autor: {e}\n")
            self.conn.rollback()
            return False

    def listar(self):
        try:
            self.cursor.execute("select * from autor order by id;")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"\nErro ao listar autores: {e}\n")
            self.conn.rollback()
            return []
        
    def buscar_id(self, id_autor):
        try:
            self.cursor.execute("select * from autor where id = %s", (id_autor,))
            return self.cursor.fetchone()
        
        except Exception as e:
            print(f"Erro ao buscar autor: {e}")
            return None    

    def atualizar(self, id_autor, nome, nacionalidade):
        try:
            if not self.existe_id("autor", id_autor):
                return False
            
            self.cursor.execute("update autor set nome=%s, nacionalidade=%s where id=%s", (nome, nacionalidade, id_autor))
            self.conn.commit()
            return True
        
        except Exception as e:
            print(f"\nErro ao atualizar autor: {e}\n")
            self.conn.rollback()
            return False

    def excluir(self, id_autor):
        try:
            if not self.existe_id("autor", id_autor):                
                return False
            
            self.cursor.execute("delete from autor where id=%s", (id_autor,))
            self.conn.commit()
            return True
        
        except Exception as e:
            print(f"\nErro ao excluir autor: {e}\n")
            self.conn.rollback()
            return False