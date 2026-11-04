class Cow:
    def __init__(self, name):  # Initializes the class with a name.
        self.image = None
        self.name = name

    def get_name(self):  # Gets the name of the cow.
        return self.name

    def get_image(self):  # Gets the image of the cow.
        return self.image

    def set_image(self, image):  # Sets an image.
        self.image = image

    def __repr__(self):  # Allows the cow to be represented as its name in a list.
        return self.name

    def __str__(self):  # Allows the cow to be represented as its name.
        return self.name
