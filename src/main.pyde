from Hull import Jarvis
from Cloud import *

win_size = 500
n_samples = 100

cloud = Cloud()
jarvis = Jarvis()

def setup():
    cloud.generate(win_size, n_samples)
    jarvis.run(cloud)
    
    size(win_size, win_size)
    background(125)

def draw():
    cloud.display()
    jarvis.display()
