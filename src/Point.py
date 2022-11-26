class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False        
                
    def display(self):
        fill(255, 0, 0)
        circle(self.x, self.y, 5)
