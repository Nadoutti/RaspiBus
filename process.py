# depois de receber uma string, esse arquivo vai buscar o onibus no banco de dados
import pandas as pd

string = '5141-10_1'
def processing(codigo):
    df = pd.read_csv('bus-dict-csv/mydb.csv')
    if 'CODIGO' in df.columns:    
        linha = df.loc[df['CODIGO'] == codigo, 'NOME'].tolist()
        if linha:
            return linha[0]
        else:
            return 'onibus nao reconhecido'
    else:
        return 'これは悪い'
