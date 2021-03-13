import numpy as np 
class Perceptron(object):
 """Perceptron classifier.

 Parameters
 ------------
 learn_rate : float
    Learning rate (between 0.0 and 1.0)
 n_iteration : int
    Passes (epochs) over the training dataset.

 Attributes
 -----------
 w_ : 1d-array
    Weights after fitting.
 errors_ : list
    Number of misclassifications in every epoch.

 """

 def __init__(self, learn_rate=0.01, n_iteration=10):
    self.learn_rate = learn_rate
    self.n_iteration = n_iteration


 def fit(self, X, y):
    """Fit training data.

    Parameters
    ----------
    X : {array-like}, shape = [n_samples, n_features]
        Training vectors, where n_samples 
        is the number of samples and
        n_features is the number of features.
    y : array-like, shape = [n_samples]
        Target values.

    Returns
    -------
    self : object

    """
    self.w_ = np.zeros(1 + X.shape[1]) # initialize to zero-vector, add 1 for the zero-weight (threshhold)
    self.errors_ = []

   # Loop thru the samples and update the weights according to the perceptron learning rule
    for _ in range(self.n_iteration):
        errors = 0
        for xi, target in zip(X, y):
            update = self.learn_rate * (target - self.predict(xi))
            self.w_[1:] += update * xi
            self.w_[0] += update
            errors += int(update != 0.0)
        self.errors_.append(errors)
    return self


 def net_input(self, X):
    """Calculate net input"""
    return np.dot(X, self.w_[1:]) + self.w_[0] # Calculate the vector dot product

# predict class labels
 def predict(self, X):
    """Return class label after unit step"""
    return np.where(self.net_input(X) >= 0.0, 1, -1)