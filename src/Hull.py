class Hull(object):
    def __init__(self):
        self.hull = []
    
    def run(self, cloud):
        raise NotImplementedError
        
    def display(self):
        for index in range(len(self.hull) - 1):
            line(self.hull[index].x, self.hull[index].y, self.hull[index + 1].x, self.hull[index + 1].y)
        
        line(self.hull[0].x, self.hull[0].y, self.hull[-1].x, self.hull[-1].y)        
    
class Jarvis(Hull):
    def __init__(self):
        super(Jarvis, self).__init__()
    
    def leftIndex(self, cloud):
        minn = cloud.__getitem__(0)
        for i in range(1,  cloud.__size__()):
            point_i = cloud.__getitem__(i)
            if point_i.x < minn.x:
                minn = point_i
            elif point_i.x == minn.x:
                if point_i.y > minn.y:
                    minn = i
        return minn
    
    def orientation(self, p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2
    
    def run(self, cloud):
        n = cloud.__size__()
        # There must be at least 3 points
        if n < 3:
            self.hull = cloud
        
        # Find the leftmost point
        l = self.leftIndex(cloud)
        p = l
        q = 0
        while(True):
            # Add current point to result
            self.hull.append(p)

            point_q = cloud.__getitem__(q)
            for i in range(n):
                # If i is more counterclockwise
                # than current q, then update q
                point_i = cloud.__getitem__(i)

                if self.orientation(p, point_i, point_q) == 2:
                    point_q = point_i
            p = point_q

            # While we don't come to first point
            if(p == l):
                break
            
class Graham(Hull):
    def __init__(self):
        super(Graham, self).__init__()
        
    def run(self, cloud):
        pass
