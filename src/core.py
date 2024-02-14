class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return (output)
    
    def forward(self, x):
        raise NotImplementedError('You must Inheritance computational!!')
    
    def backward(self, gy):
        raise NotImplementedError('You must Inheritance computational!!')