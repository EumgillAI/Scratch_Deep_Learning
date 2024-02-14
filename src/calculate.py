import numpy as np

from core import Function

class Exp(Function):
    def forward(self, x):
        return np.exp(x)
