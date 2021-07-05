# The lines are color coded according to their labels: blue for R (rock), and red for M (mine). Sometimes a plot of this type will show clear areas of separation between the classes. For the rocks versus mines data set, no extremely clear separation is evident in the line plot, but there are some areas where the blues and reds are separated. Along the bottom of the plot, the blues stand out a bit, and in the range of attribute indices from 30 to 40, the blues are somewhat higher than the reds. These kinds of insights can help in interpreting and confirming predictions made by your trained model.

import pandas as pd 
from pandas import DataFrame 
import matplotlib.pyplot as plot 
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#read rocks versus mines data into pandas data frame 
rocksVMines = pd.read_csv(target_url,header=None, prefix="V") 

for i in range(208): 
    #assign color based on "M" or "R" labels 
    if rocksVMines.iat[i,60] == "M": 
        pcolor = "red" 
    else: 
        pcolor = "blue" 

    #plot rows of data as if they were series data 
    dataRow = rocksVMines.iloc[i,0:60] 
    dataRow.plot(color=pcolor) 

plot.xlabel("Attribute Index") 
plot.ylabel(("Attribute Values")) 
plot.show()