class CollisionHandler(object):
    def __init__(self):
        pass

    def calculate_collisions(self, units):
        for unit in units:
            collision_object = unit.rect.collidelist(units)
            if collision_object != -1:
                pass
