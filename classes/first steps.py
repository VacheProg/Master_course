# keteri kordinat ->>> tuple tupleneri zuygeri
# tuple koxeri erkarutyuneri
from math import sqrt

# erankyun = input("Mutqagreq erankyun ")# (0, 0) : (0, 3) : (4, 0)
#V1


def get_distance(p1, p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def get_area(points):
    a = get_distance(points[0], points[1])
    b = get_distance(points[1], points[2])
    c = get_distance(points[0], points[2])
    perimeter = a + b + c
    area = sqrt(perimeter * (perimeter-a) * (perimeter-b) * (perimeter-c))
    return  area

def is_equal_points(points):
    pass

def get_obj_from_string(txt):
    points = [eval(i.strip()) for i in txt.split(":")]
    if False and (not is_equal_points(points)):
        raise Exception("chenq kara anenq")
    print("area equals: ", get_area(points))



# print(get_obj_from_string(erankyun)) #((), (), ())
# print(sqrt(12*9*8*7))


class Points:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Points(self.x-other.x, self.y-other.y)

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"


class Triangle:


    def __init__(self, points, is_uxankyun=False):
        self.points = points

    def get_area(self):
        a = get_distance(self.points[0], self.points[1])
        b = get_distance(self.points[1], self.points[2])
        c = get_distance(self.points[0], self.points[2])
        perimeter = a + b + c
        area = sqrt(perimeter * (perimeter - a) * (perimeter - b) * (perimeter - c))
        return area


random_point = Points(5,9)
random_point1 = Points(10,20)

print(random_point)
print(random_point-random_point1)

# p = []
# for i in [(1,2), (4,6), (5,8)]:
#     p.append(Points(*i))
#
# print(p)
# t1 = Triangle([(1,2), (4,6), (5,8)], is_uxankyun=True)

# print(t1.get_area())



