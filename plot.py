import pandas as pd
import matplotlib.pyplot as plt

FILE = "BCD.xls"
df = pd.read_excel(FILE, skip = 1, header = 1, index_col = 'DATE')
print(df.head())

doc = """GDP5	PROD5
IND	MANUF
STROI	AGRO
OPT	RETAIL
CARGO	PASS
INV	COMM"""
pairs = [x.split("\t") for x in doc.split("\n")]

# 6 subplots, the axes array is 1-d
f, axarr = plt.subplots(6, sharex=True, figsize = (5, 12))

for i in range(6):
    axarr[i].plot(df[pairs[i]])
    title = "+".join(pairs[i])
    axarr[i].set_title(title)
    

plt.savefig('plot.png')
