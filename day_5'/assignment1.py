import math
class Circle:
    pass

def create(radius):
    c = Circle()
    c.radius = radius
    return c

def is_valid(c):
    return isinstance(c,Circle) and c.radius > 0

def area(c):
    
     return math.pi * c.radius **2 


def perimeter(c):
    
     return 2 * math.pi * c.radius 

def info(c):
    return f'Circle<{c.radius}>' if is_valid(c) else '<invalid circle>'

def draw(c):
    print(info(c))

def model_circle(r):
    c = create(r)
    draw(c)
    
    if is_valid(c):
     print(f'Area={area(c)}')
     print(f'Perimeter={perimeter(c)}')
    
        
if __name__ == "__main__":
    model_circle(7)





    
