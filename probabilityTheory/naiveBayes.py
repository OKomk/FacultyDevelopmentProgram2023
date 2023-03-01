import numpy as np
import pandas as pd

class NaiveBayesClassifier:
    def __init__(self):
        self.prior = None
        self.mean = None
        self.variance = None
    
    def fit(self, X, y):
        # Calculate prior probabilities
        self.prior = [np.sum(y == c) / len(y) for c in np.unique(y)]
        
        # Estimate class-conditional probabilities
        self.mean = [np.mean(X[y == c]) for c in np.unique(y)]
        self.variance = [np.var(X[y == c]) for c in np.unique(y)]
    
    def predict(self, X):
        # Calculate posterior probabilities
        posterior = [np.log(self.prior[c]) - 0.5*np.log(2*np.pi*self.variance[c]) - 0.5*((X - self.mean[c])/self.variance[c])**2 for c in range(len(self.prior))]
        
        # Make classification
        return np.argmax(posterior)

