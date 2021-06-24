class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
    def funk(self,x,y):
        print(x, y)
        my=self.z
        print(my)
        return my
pt = Point(3,4)
print(pt.funk(4,5))