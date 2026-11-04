class Cow:
    def __init__(self, name):
        self.image = None
        self.name = name

    def get_name(self):
        return self.name

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
