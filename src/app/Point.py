class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def display(self):
        fill(255, 0, 0)
        circle(self.x, self.y, 5)
