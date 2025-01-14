from dbfread import DBF
import pandas as pd



dbf = DBF('bus-dict/LB15_LI_MSP_CEM_V3.dbf', encoding='latin-1')

df = pd.DataFrame(iter(dbf))

df.to_csv('bus-dict-csv\mydb.csv', index=True)
print('deu certo')