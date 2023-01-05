from calc import calculate_distance
import pygame

EYE_SIGHT_DISTANCE = 200

class SightHandler(object):
    def __init__(self):
        pass

    def update_eyesight(self, units, screen): #todo fix to 120 degrees instead of 360
        for unit in units:
            seen = []
            if unit.type == "unit":
                for other_unit in units:
                    distance_unit_other_unit = calculate_distance(unit, other_unit)
                    if distance_unit_other_unit < EYE_SIGHT_DISTANCE and unit != other_unit:
                        line = (unit.rect.center, other_unit.rect.center)
                        if self.check_if_sight_is_blocked(line, units):
                            seen.append([other_unit.type, other_unit.rect.centerx, other_unit.rect.centery])             #todo add type what you see
                            pygame.draw.line(screen, (0, 0, 0), unit.rect.center, other_unit.rect.center)
                unit.update_eye_sight(seen)

            #pick the front 120 degree
            #find if an unit is in here
            #if so, add it to the unit his list.
    def check_if_sight_is_blocked(self, line, units):
        for unit in units:
            if unit.type == "wall":
                if unit.rect.clipline(line):
                    return False
        return True


#@numba.njit()
