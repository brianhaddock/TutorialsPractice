from sklearn.datasets import load_iris 
data = load_iris() 
print ("Features :%s" % data.feature_names) 
features = data.data 
labels = data.target  

