class CollisionHandler(object):
    def __init__(self):
        pass

    def calculate_collisions(self, units):
        for unit in units:
            if unit.type == "unit":
                for other_unit in units:
                    collision_objects = unit.rect.colliderect(other_unit)
                if collision_objects != 0:
                    unit.add_collision(collision_objects)
                    print("BOTS")
                else:
                    unit.remove_collision()

