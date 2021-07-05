import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create table of test values 
data =\
[
[0, 1],
[1, 8],
[2, 13],
[3, 16],
[4, 20],
]

# Reshape table of test values into two arrays
X = np.array(data)[:,0].reshape(-1,1)
y = np.array(data)[:,1].reshape(-1,1)
print("X=")
print(X)
print("y=")
print(y)

#This is the next values to predict (convert to array)
to_predict_x= [5,6,7]
to_predict_x= np.array(to_predict_x).reshape(-1,1)

# Use the LinearRegression() method from sklearn library and 
# create a regressor object. We then call the fit() method on 
# the regressor object and pass the parameters X and y. The 
# fit() method is used to train our program and basically 
# come up with a straight line that fits our data.
regsr=LinearRegression()
regsr.fit(X,y)

#Now, we can predict the values for a given position by passing the 
#“to_predict_x” variable to the predict() method. This 
#will predict the y-values for the given x-values using 
#the extrapolation method. We can also get the slope(m) 
#and y-intercept(c) of the fitted line.
predicted_y= regsr.predict(to_predict_x)
m= regsr.coef_
c= regsr.intercept_
print("Predicted y:\n",predicted_y)
print("slope (m): ",m)
print("y-intercept (c): ",c)

# We want to see how the line that we fitted to the inputs look
import matplotlib.pyplot as plt
plt.title('Predict the next numbers in a given sequence')  
plt.xlabel('X')  
plt.ylabel('Numbers') 
plt.scatter(X,y,color="blue")
new_y=[ m*i+c for i in np.append(X,to_predict_x)]
new_y=np.array(new_y).reshape(-1,1)
plt.plot(np.append(X,to_predict_x),new_y,color="red")
plt.show()