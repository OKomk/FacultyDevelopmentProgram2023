import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt

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

df = pd.read_csv('Naive-Bayes-Classification-Data.csv')
print(df)

plt.hist(df["glucose"])
plt.show()
plt.hist(df["bloodpressure"])
plt.show()


X_train, X_test, y_train, y_test = train_test_split(df[["glucose","bloodpressure"]], df["diabetes"], test_size=0.3, random_state=42)
print(X_train)
print(y_train)


model = NaiveBayesClassifier()
model.fit(X_train["glucose"],y_train)
y_pred = model.predict(X_test["glucose"])
print(y_pred)
# cm = confusion_matrix(y_test,y_pred)
# print(cm)



