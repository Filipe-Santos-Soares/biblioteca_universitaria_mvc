import psycopg2

class BibliotecaModel:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname="biblioteca",
                user="postgres",
                password="admin",
                host="localhost",
                port="5432"
            )
            self.cursor = self.conn.cursor()
            print("\nConexão estabelecida com sucesso!\n")
        except Exception as e:
            print(f"\nFalha ao conectar ao banco de dados: {e}\n")

    def existe_id(self, tabela, id_valor):
        try:
            self.cursor.execute(f"select 1 from {tabela} where id=%s;", (id_valor,))
            return self.cursor.fetchone() is not None
        except Exception as e:
            print(f"\nFalha ao verificar: {e}\n")
            return False        

    def __del__(self):
        if hasattr(self, "cursor") and hasattr(self, "conn"):
            self.cursor.close()
            self.conn.close()
            print("\nConexão encerrada.\n")