from cow import Cow


class Dragon(Cow):

    def __init__(self, name, image):  # Initializes as a subclass of Cow.
        super().__init__(name)
        self.image = image

    def can_breath_fire(self):  # Returns that the dragon can breathe fire.
        return True
