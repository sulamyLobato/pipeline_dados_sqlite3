import pandas as pd
import sqlite3

class ExtracaoDados:
    @staticmethod
    def carregar_tabela_sqlite3(tabela, nome_banco):
        conn = sqlite3.connect(nome_banco)
        query = f"SELECT * FROM {tabela}"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df

    @staticmethod
    def carregar_csv(path):
        df = pd.read_csv(path, sep=";")
        return df
