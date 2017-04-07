"""
Macroeconomic time series - illustation based on 
Russian economic trends and Business Conditions Digest.

"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
#
# Data inputs
#
#------------------------------------------------------------------------------

FILE = "BCD.xls"
df = pd.read_excel(FILE, 0, skip=1, header=1, index_col='DATE')
df = df.applymap(lambda x: np.nan if x == 0 else x)
print(df.head())
df[['GDP5']] = df[['GDP5']].fillna(method='bfill', limit=12)

plot_title = "Plot title"

doc = """GDP5	PROD5
IND	MANUF
STROI	AGRO
OPT	RETAIL
CARGO	PASS
INV	COMM"""
pairs = [x.split("\t") for x in doc.split("\n")]


#------------------------------------------------------------------------------
#
# Drawing
#
#------------------------------------------------------------------------------

# 6 subplots
def draw_6(df, pairs):
    """
    df - dataframe with time series to plot
    pairs - list of varname pairs e.g. [['GDP5', 'PROD5'],
                                       ['IND', 'MANUF']]
    """
    f, axarr = plt.subplots(6, sharex=True, figsize=(6, 12))
    
    for i, (ax, pair) in enumerate(zip(axarr, pairs)):
        ax.plot(df[pair])
        ax.legend(pair, loc=2, prop={'size': 8}, fancybox=True, framealpha=1.0).get_frame().set_edgecolor('none')
        ax.grid(True)
        ax.set_ylim() # bottom=0
        ax.set_xlim(left='1990-01-01',  right='2018-01-01')
        if i == 0:
            ax.spines['top'].set_visible(True)
            ax.spines['bottom'].set_visible(False)
            ax.tick_params(
                    axis='x',          
                    which='both',     
                    bottom='off',    
                    top='off',      
                    labelbottom='off')
            ax.yaxis.set_major_locator(MaxNLocator(prune='lower'))
        elif i <= 4:
            ax.spines['top'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.tick_params(
                    axis='x',          
                    which='both',     
                    bottom='off',    
                    top='off',      
                    labelbottom='off')
            ax.yaxis.set_major_locator(MaxNLocator(prune='lower'))
        else:
            ax.spines['top'].set_visible(False)
            ax.spines['bottom'].set_visible(True)
            ax.tick_params(
                    axis='x',        
                    which='both',   
                    bottom='on',   
                    top='off',    
                    labelbottom='on')
    
    plt.subplots_adjust(wspace=0.0, hspace=0)
    axarr[0].set_title(plot_title)
    return f

f1 = draw_6(df, pairs)
plt.savefig('plot.png', bbox_inches='tight')

def draw_12(df, labs):
    f, axarr = plt.subplots(12, sharex=True, figsize=(4, 12))
    for i, (ax, lab) in enumerate(zip(axarr, labs)):
        ax.plot(zf[lab])
        ax.grid()

        ax.set_xlim(left='2016-01-01',  right='2017-06-01')
        ax.legend(lab, loc=1).get_frame().set_edgecolor('none')
        if i < 11: 
            ax.tick_params(
                    axis='x',          
                    which='both',     
                    bottom='off',    
                    top='off',      
                    labelbottom='off')            

labs = ['GDP5' , 'PROD5', 'IND', 'MANUF',  
        'STROI',	'AGRO' , 'OPT', 'RETAIL',
        'CARGO',	'PASS' , 'INV', 'COMM'] 
zf = df.loc['2016-01-01':,:]
f2 = draw_12(zf, labs)
plt.savefig('plot2.png', bbox_inches='tight')



"""
Session 2.1 - draw_6() + draw_12() + combination
=================================================

Todo:
    
draw_6():
    - can we add a right-hand side y axis with labels too? 
      same as left labels.
      
draw_12():
    - legend is just one letter, can fix it? same label as in draw_6()
    - less x axis labels - only year starts? (grid is ok)    
    
combination:    
    - can we combine two plots horizonatally - draw_6() on right 
    and draw 12() on left.
    
Fancy (comment or do if any time remains):
    - pick same color for plots in draw_12, from 
      on my machine 
    - last datapoint on draw_12 
       - make it a larger dot
       - add value as text to the rigth of dot
       - combine value and date in text as "101.2\n(02.2017)"
       
Note (not todo):
    - three labels in graph draw_12() is too much, 2 is good
    - may need to relabel
    
Session 2.2. - shaded vertical bars
===================================

Need to add shaded vertical bars on graphs as in 
https://fred.stlouisfed.org/series/A191RL1Q225SBEA

In Excel we use barplots for this. See example in shaded.xls

starts and ends of shaded bars is in *recessions*. endpoints are included in shaded area
"""

recessions = [['1998-01', '1999-01'],
              ['2008-08', '2009-09'], 
              ['2015-01', '2016-06']]




"""
Session 1.
=========
Easy *DONE:
1. Set vertical space between subplots to 0 *DONE
2. No ticks on x axis on plots 0-4 (0-based) *DONE
3. Transparent lower and upper boundary of plot for subplots 1-4 (0-based) *DONE
4. Legend on each subplot, control its location - upper left corner *DONE
5. Vertical grid on each suplot *DONE
6. Horizontal grid on each suplot *DONE
7. Global header for the enire plot *DONE

Not that easy *DONE:
8. df.GDP5 is by quarter, still want to put it on first subplot *DONE
9. Suggestions to control figure size. Currently figsize=(6, 12)
   was trail and error. *WONTFIX
10. Saveing to png adds whitespace on top of graph. 
   Possible to eliminate? *DONE
"""

"""
Comments
========
- Названия, размерность
- Шейдинг рецессий
- Лидирующие индикаторы / цикличность
- Показывать оси справа
- Долгосрочные и краткокрочные - последние еще группа графиков справа
<http://conference.scipy.org/proceedings/scipy2015/pdfs/mellissa_cross_t.pdf>
- save df to csv or Excel 
"""