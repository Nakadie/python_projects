class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y :
            return True
    
    def __repr__(self) -> str:
        return  "Coordinate(%d,%d)" % (self.x, self.y)
X = 7
Y = 8
c1 = Coordinate(17, 17)
c2 = Coordinate(17, 17)
print(c1 == c2)

