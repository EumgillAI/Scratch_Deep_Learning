import numpy as np 

from function import Function

class Square(Function):
    def forward(self, x):
        return (x ** 2)

class Exp(Function):
    def forward(self, x):
        return np.exp(x)