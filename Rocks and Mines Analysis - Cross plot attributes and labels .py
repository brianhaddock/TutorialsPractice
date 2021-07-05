# Another question you might ask of the data is how the various attributes relate to one another. One quick way to get an idea of pair-wise relationships is to cross-plot the attributes with the labels. Listing 2-7 shows what’s required to generate cross-plots for a couple of representative pairs of attributes. These cross-plots (also called scatter plots) show you how closely related the pairs of variables are.

import pandas as pd 
from pandas import DataFrame 
import matplotlib.pyplot as plot 
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#read rocks versus mines data into pandas data frame 
rocksVMines = pd.read_csv(target_url,header=None, prefix="V") 

#calculate correlations between real-valued attributes 
# Pandas' loc works on labels while iloc works on positions. ix behaves like loc but falls back to behaving like iloc if the label is not in the index. The following line extracts row 1, columns 1 through 61 (it's zero-index based) - the 60 samples taken at 60 different frequencies
dataRow2 = rocksVMines.iloc[1,0:60] 
dataRow3 = rocksVMines.iloc[2,0:60] 

plot.scatter(dataRow2, dataRow3) 

plot.xlabel("2nd Attribute") 
plot.ylabel(("3rd Attribute"))
plot.show() 

dataRow21 = rocksVMines.iloc[20,0:60] 

plot.scatter(dataRow2, dataRow21) 

plot.xlabel("2nd Attribute") 
plot.ylabel(("21st Attribute")) 
plot.show()