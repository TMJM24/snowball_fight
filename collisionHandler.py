class CollisionHandler(object):
    def __init__(self):
        pass

    def calculate_collisions(self, units):
        for unit in units:
            if unit.type == "unit":
                unit.remove_collision()
                for other_unit in units:
                    if unit == other_unit:
                        pass
                    elif unit.rect.colliderect(other_unit):
                        unit.add_collision(other_unit)
                        print("BOTS")

