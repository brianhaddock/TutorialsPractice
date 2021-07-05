import urllib2

import sys 

#NOTE: I was unable to install urllib2 and thus, this script will not run.
# urllib2 is only available for Python 2.1.

#read data from uci data repository 
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib2.urlopen(target_url) 

#arrange data into list for labels and list of lists for attributes 
xList = [] 
labels = [] 
for line in data: 
    #split on comma 
    row = line.strip().split(",") 
    xList.append(row) 
    
sys.stdout.write("Number of Rows of Data = " + str(len(xList)) + '\n') 
sys.stdout.write("Number of Columns of Data = " + str(len(xList[1])))