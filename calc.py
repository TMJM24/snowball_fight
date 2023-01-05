import math

def calculate_distance_rect(obj1, obj2):
    x_difference = obj1.rect.centerx - obj2.rect.centerx
    y_difference = obj1.rect.centery - obj2.rect.centery
    return math.sqrt(((x_difference * x_difference) + (y_difference * y_difference)))

def calculate_distance(obj1, obj2):
    x_difference = obj1[0] - obj2[0]
    y_difference = obj1[1] - obj2[1]
    return math.sqrt(((x_difference * x_difference) + (y_difference * y_difference)))
