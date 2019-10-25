import pandas as pa

data = pa.read_csv('readexcel.csv', low_memory=False)

print(data[5:8])