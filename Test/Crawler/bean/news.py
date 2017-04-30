__metaclass__ = type


class News:

    def __init__(self, image1, image2, image3, title, source, link):
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3
        self.title = title
        self.source = source
        self.link = link

    def get_image1(self):
        return self.image1

    def get_image2(self):
        return self.image2

    def get_image3(self):
        return self.image3

    def get_title(self):
        return self.title

    def get_source(self):
        return self.source

    def get_link(self):
        return self.link
