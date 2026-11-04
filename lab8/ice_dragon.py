from dragon import Dragon


class IceDragon(Dragon):

    def __init__(self, name, image):  # Initializes as a subclass of Dragon.
        super().__init__(name, image)

    def can_breath_fire(self):  # Returns that ice-dragon cannot breathe fire.
        return False
