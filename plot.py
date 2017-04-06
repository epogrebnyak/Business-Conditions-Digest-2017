import pandas as pd
import matplotlib.pyplot as plt

FILE = "BCD.xls"
df = pd.read_excel(FILE, skip=1, header=1, index_col='DATE')
print(df.head())

doc = """GDP5	PROD5
IND	MANUF
STROI	AGRO
OPT	RETAIL
CARGO	PASS
INV	COMM"""
pairs = [x.split("\t") for x in doc.split("\n")]

# 6 subplots, the axes array is 1-d
f, axarr = plt.subplots(6, figsize=(6, 12))

for i in range(6):
    axarr[i].plot(df[pairs[i]])
    # title = "+".join(pairs[i])
    # axarr[i].set_title(title)
    #5&6
    axarr[i].grid(True)
    #4
    axarr[i].legend(pairs[i], loc='upper left')
    axarr[i].set_xlim('1995','2018')
    
    if i in range(0,4):
        #2
        axarr[i].xaxis.set_major_formatter(NullFormatter())
        #3
        axarr[i].spines['top'].set_visible(False)
        axarr[i].spines['bottom'].set_visible(False)

#7
f.suptitle('GlobalTitle', fontsize=15)
#1 h_pad padding (height) between subplots.
plt.tight_layout(pad=3, h_pad=.2)

plt.savefig('plot.png')

"""

Easy:
1. Set vertical space between subplots to 0
2. No ticks on x axis on plots 0-4 (0-based) 
3. Transparent lower and upper boundary of plot for subplots 1-4 (0-based) 
   (is it possible?)
4. Legend on each subplot, control its location - upper left corner
5. Vertical grid on each suplot
6. Horizontal grid on each suplot
7. Global header for the enire plot

Not that easy:
8. df.GDP5 is by quarter, still want to put it on first subplot
9. Suggestions to control figure size. Currently figsize=(6, 12)
   was trail and error.
10. Saveing to png adds whitespace on top of graph. Possible to eliminate?
"""

# not todo
# - save df to csv or Excel 
# - bars for recession
# - delete zeros
