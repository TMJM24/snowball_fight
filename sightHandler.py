from calc import calculate_distance_rect, calculate_angle
from game_object import game_obj
import pygame
import math

EYE_SIGHT_DISTANCE = 200
DEGREES = 180

class SightHandler(object):
    def __init__(self):
        pass

    def update_eyesight(self, units: list, screen: pygame.Surface): #todo fix to 120 degrees instead of 360
        for unit in units:
            seen = []
            if unit.type == "unit":
                for other_unit in units:
                    distance_unit_other_unit = calculate_distance_rect(unit, other_unit)
                    if distance_unit_other_unit < EYE_SIGHT_DISTANCE and unit != other_unit:

                        line = (unit.rect.center, other_unit.rect.center)
                        if self.check_if_sight_is_blocked(line, units, unit, other_unit):

                            angle = math.radians(unit.angle)
                            right_in_front = [(math.sin(angle)) * EYE_SIGHT_DISTANCE + unit.rect.centerx,
                                              (math.cos(angle)) * EYE_SIGHT_DISTANCE + unit.rect.centery]
                            angle = calculate_angle(unit.rect.center, right_in_front, other_unit.rect.center)
                            #print(f"angle is {angle}")
                            if angle > 0:
                                seen.append([other_unit.type, other_unit.rect.centerx, other_unit.rect.centery])             #todo add type what you see
                                pygame.draw.line(screen, (0, 0, 0), unit.rect.center, other_unit.rect.center)
                unit.update_eye_sight(seen)

            #pick the front 120 degree
            #find if an unit is in here
            #if so, add it to the unit his list.
    def check_if_sight_is_blocked(self, line: tuple, units: list, unit1: game_obj, unit2: game_obj) ->bool:

        for unit in units:
            if unit == unit1 or unit == unit2:
                pass
            elif unit.rect.clipline(line):
                return False
        return True


#@numba.njit()
