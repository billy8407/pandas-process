import pandas as pd
import os
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
delte_row_index=[]

new_date = True

for row in range(500):
    maturity_month = df.loc[row, 'maturity_month'].replace(' ','')
    if len(maturity_month) != 6:
        delte_row_index.append(row)
    
    elif new_date == True:
        now_date = df.loc[row, 'date']
        new_date = False
    
    elif df.loc[row, 'date'] == now_date:
        pass
    
    else:
        delte_row_index.append(row)

df = df.drop(delte_row_index, axis=0)

print(df)