import math


EYE_SIGHT_DISTANCE = 200

class SightHandler(object):
    def __init__(self):
        pass

    def update_eyesight(self, units): #todo fix to 120 degrees instead of 360
        for unit in units:
            seen = []
            if unit.type == "unit":
                for other_unit in units:
                    distance_unit_other_unit = calculate_distance(unit, other_unit)
                    if distance_unit_other_unit < EYE_SIGHT_DISTANCE and unit != other_unit:
                        seen.append([other_unit.type, other_unit.rect.centerx, other_unit.rect.centery])             #todo add type what you see
                unit.update_eye_sight(seen)

            #pick the front 120 degree
            #find if an unit is in here
            #if so, add it to the unit his list.
        pass

#@numba.njit()
def calculate_distance(obj1, obj2):
    x_difference = obj1.rect.centerx - obj2.rect.centerx
    y_difference = obj1.rect.centery - obj2.rect.centery
    return math.sqrt(((x_difference * x_difference) + (y_difference * y_difference)))
