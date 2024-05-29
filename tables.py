import pandas as pd
import numpy as np

def readEx(file):
    table = pd.read_excel(io=file, engine='odf')
    #print("Excel file readed:" + str(table))
    return table

def numerateRows(table):
    numCol = [i+1 for i in range(0, len(table))]
    table.insert(loc=0, column='№', value=numCol)
    return table

def replaceCols(table, col1,col2):
    cols = list(table.columns)
    first, second = cols.index(col1), cols.index(col2)
    cols[first], cols[second] = cols[second], cols[first]
    table = table[cols]
    return table


def genHtmlTable(table):
    table.style
    result = table.to_html(index=False)
    result = result.replace('NaN', '')
    result = result.replace('.', ',')
    result = result.replace(',ru', '.ru')
    return result