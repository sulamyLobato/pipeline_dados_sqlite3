import sqlite3
import pandas as pd


class GerenciadorBanco:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
    
    def criar_banco_dados(self):
        conn = sqlite3.connect(self.nome_banco)
        print("Banco criado com sucesso!")
        conn.close()
    
    def criar_tabela(self, tabela, colunas):
        conn = sqlite3.connect(self.nome_banco)
        cursor = conn.cursor()
        
        colunas_query = ", ".join([f"{coluna} {tipo}" for coluna, tipo in colunas.items()])
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {tabela} (
                {colunas_query}
            );
        """)
        
        conn.commit()
        conn.close()
        print(f"Tabela '{tabela}' criada com sucesso!")
    
    def listar_tabelas(self):
        conn = sqlite3.connect(self.nome_banco)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tabelas = cursor.fetchall()
        conn.close()
        
        for tabela in tabelas:
            print(tabela[0])



    def inserir_dados(self, tabela, df):
        conn = sqlite3.connect(self.nome_banco)
        cursor = conn.cursor()
        # Gerando a query automaticamente com base nas colunas do DataFrame
        colunas_query = ', '.join(df.columns)
        placeholders = ', '.join(['?' for _ in df.columns])
        sql = f"INSERT INTO {tabela} ({colunas_query}) VALUES ({placeholders})"

        try:
            cursor.executemany(sql, df.values.tolist())  # Inserindo os dados
            conn.commit()
            print(f"{len(df)} registros inseridos com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")
        finally:
            conn.close()


    def listar_dados(self, tabela):
 
        conn = sqlite3.connect(self.nome_banco)
        cursor = conn.cursor()

        try:
            df = pd.read_sql_query(f"SELECT * FROM {tabela};", conn)
            return df
        except Exception as e:
            print(f"Erro ao buscar dados: {e}")
            return pd.DataFrame()
        finally:
            conn.close()

       












  






