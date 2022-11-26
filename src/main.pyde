from Cloud import *

win_size = 500
n_samples = 20

cloud = Cloud()

def setup():
    cloud.generate(win_size, n_samples)
    
    size(win_size, win_size)
    background(125)

def draw():
    cloud.display()
