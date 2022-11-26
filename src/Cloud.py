import random

from Point import *

class Cloud:
    def __init__(self, offset = 50):
        self.offset = 50
        self.cloud = []
    
    def __size__(self):
        return len(self.cloud)

    def __getitem__(self, index):
        try:
            return self.cloud[index]
        except IndexError:
            return None
            print("Index should be smaller.")
        
    def __add__(self, p):
        self.cloud.append(p)    
    
    def generate(self, w_size, n_samples):
        while len(self.cloud) < n_samples:
            x = random.randint(self.offset, w_size-self.offset)
            y = random.randint(self.offset, w_size-self.offset)

            p = Point(x, y)
            self.__add__(p)
            
    def display(self):
        for p in self.cloud:
            p.display()
