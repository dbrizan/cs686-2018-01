from classifier import classifier
import numpy as np


class logistic_regression(classifier):

    def __init__(self, cycles):
        self.alpha = 0.001
        self.maxcycles = cycles
        self.weights = None  # Placeholder for later...


    def sigmoid(self, x):
        return 1.0 / (1 + np.exp(-x))


    def fit(self, Xin, Yin):
        print 'Logistic Regression classifier - fit'

        X = np.mat(Xin)
        Y = np.mat(Yin).transpose()
        m, n = X.shape
        self.weights = np.ones((n, 1))
        for k in range(self.maxcycles):
            h = self.sigmoid(X * self.weights)
            error = (Y - h)
            self.weights = self.weights + self.alpha * X.transpose() * error
        return self.weights
 

    def predict(self, X):
        print 'Logistic Regression classifier - predict'

