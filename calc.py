import math

def calculate_distance_rect(obj1, obj2):
    x_difference = obj1.rect.centerx - obj2.rect.centerx
    y_difference = obj1.rect.centery - obj2.rect.centery
    return math.sqrt(((x_difference * x_difference) + (y_difference * y_difference)))

def calculate_distance(obj1, obj2):
    x_difference = obj1[0] - obj2[0]
    y_difference = obj1[1] - obj2[1]
    return math.sqrt(((x_difference * x_difference) + (y_difference * y_difference)))

def slope_points(p1, p2):
    return (p2[1]-p1[1])/(p2[0]-p1[0])

def slope(x1, y1, x2, y2): # Line slope given two points:
    if x2 - x1 == 0:
        x2 += 0.001
    return (y2-y1)/(x2-x1)

def angle(s1, s2):
    return math.degrees(math.atan((s2-s1)/(1+(s2*s1))))

def calculate_angle(unit_center, unit_infront, unit_target):
    lineA = (unit_center, unit_infront)
    lineB = (unit_center, unit_target)

    slope1 = slope(lineA[0][0], lineA[0][1], lineA[1][0], lineA[1][1])
    slope2 = slope(lineB[0][0], lineB[0][1], lineB[1][0], lineB[1][1])
    ang = angle(slope1, slope2)
    return ang

if __name__ == "__main__":
    lineA = ((0.6, 3.6), (1.6, 3))
    lineB = ((1.6, 3), (2, 3.6))

    slope1 = slope(lineA[0][0], lineA[0][1], lineA[1][0], lineA[1][1])
    slope2 = slope(lineB[0][0], lineB[0][1], lineB[1][0], lineB[1][1])

    ang = angle(slope1, slope2)
    print('Angle in degrees = ', ang)
