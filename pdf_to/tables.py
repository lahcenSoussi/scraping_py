from tabula import read_pdf
import pandas as pd

try:
    tables = read_pdf("file.pdf", pages='all')
    df = tables[0]
    print(df)
    df.to_csv('table.csv', index=False)
    print('Done')
except Exception as e:
    print(e)
