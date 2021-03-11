import pandas as pd

import os
import sys

file_name = input('請輸入 excel 名稱(xlsx 檔): ')
print('程式啟動中...')
#xlsx_name = "../finance_data/" + file_name + ".csv"

xlsx_name = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "\\finance_data\\" + file_name + ".csv"
print(xlsx_name)
#print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
df = pd.read_csv(xlsx_name)


df_columns = list(df.columns)




using_col_list = ['date','maturity_month','transaction_time','transaction_price','transaction_volume']
for col in df_columns:
    if col not in using_col_list:
        del df[col]



row_num = df.shape[0]
delete_row_index=[]

new_date = True
new_maturity_month = ''

for row in range(2000):
    maturity_month = df.loc[row, 'maturity_month'].replace(' ','')
    if len(maturity_month) != 6:
        delete_row_index.append(row)
    
    if new_date == True:
        now_date = df.loc[row, 'date']
        new_maturity_month = maturity_month 
        new_date = False
    
    else:
        if now_date == df.loc[row, 'date']:
            if new_maturity_month != df.loc[row, 'maturity_month'].replace(' ',''):
                delete_row_index.append(row)
            else:
                pass
        else: #重置excel
            now_date = df.loc[row, 'date']
            new_maturity_month = maturity_month 
            


    

df = df.drop(delete_row_index, axis=0)

df.to_csv('%s_output.csv' %file_name, encoding=sys.getfilesystemencoding(),index=False)
#print(df)