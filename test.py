import pandas as pd
import numpy as np

filename='dose_protonPDD10.out'

skiprow=0

with open(filename,'r') as ff:     
       for i, row in enumerate(ff):
           if "h:" in row:
                   skiprow=i
#                   print i
skiprow+=1

skipfoot=0

with open(filename,'r') as ff:     
       for i, row in enumerate(ff):
           if "'no." in row:
                   skipfoot=i
#                   print i
skipfoot-=4
skipft=skipfoot-skiprow
#print skipft

columns = ['z-lower','z-upper','proton','r.err']

df=pd.read_table(filename,delim_whitespace=True,header=None,names=columns,skiprows=skiprow,nrows = skipft)

df.to_csv('dose_protonPDD10.csv',sep=',')
