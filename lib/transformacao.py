import pandas as pd



class Transformacao:
    def __init__(self, df):
      
        self.df = df


        

    def renomear_colunas(self, mapeamento_colunas):
     
        if not isinstance(mapeamento_colunas, dict):
            raise ValueError("O mapeamento de colunas deve ser um dicionário.")
        
        self.df = self.df.rename(columns=mapeamento_colunas)
        return self.df
    

    def remover_duplicatas(self, df):
       
        return df.drop_duplicates()








