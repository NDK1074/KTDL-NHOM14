import pandas as pd

# Lưu ý: file csv này dùng dấu chấm phẩy ';' để phân cách cột
df = pd.read_csv('../data/raw/wine.csv', sep=';')
print(df.head())