# depois de receber uma string, esse arquivo vai buscar o onibus no banco de dados
import pandas as pd

string = '5141-10_1'
def processing(codigo):
    df = pd.read_csv('bus-dict-csv/mydb.csv')
    if 'LINHA_CODI' in df.columns:    
        linha = df.loc[df['LINHA_CODI'] == codigo, 'NOME'].tolist()
        if linha:
            return linha[0]
        else:
            return 'onibus nao reconhecido'
    else:
        return 'これは悪い'
