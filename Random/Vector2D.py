import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y        
            
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
def Main():
    vec = Vector2D(5, 6)
    print('vector 1: \nX: ' + str(vec.x) + ',Y: ' + str(vec.y))

if __name__=='__main__':
    Main()
