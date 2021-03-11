import pandas as pd
file_name = input('請輸入 excel 名稱(xlsx 檔): ')
print('程式啟動中...')
xlsx_name = "finance_data/" + file_name + ".csv"
df = pd.read_csv(xlsx_name)
print(df.shape)
