import random

from Point import *

class Cloud:
    def __init__(self, offset = 50):
        self.offset = 50
        self.cloud = []
    
    def addPoint(self, p):
        self.cloud.append(p)    
    
    def generate(self, w_size, n_samples):
        while len(self.cloud) < n_samples:
            x = random.randint(self.offset, w_size-self.offset)
            y = random.randint(self.offset, w_size-self.offset)

            p = Point(x, y)
            self.addPoint(p)
            
    def display(self):
        for p in self.cloud:
            p.display()
