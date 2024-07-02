import pandas as pd


class Imbaud:
    def salvar_excel(self):
        df = pd.read_parquet(r"C:\Users\gabri\OneDrive\Data Analytics\03 - DataLake\Comparin\01-Imbaud\vendas.parquet")
        df = df[df['Id Filial'] == 1]
        df.to_excel(r"C:\Users\gabri\Downloads\Temp.xlsx")
        return df
