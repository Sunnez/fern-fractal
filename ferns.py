from PIL import Image


class BarnsleyFern(object):
    def __init__(self, width, height, color='black', background_color='white'):
        super(Fern, self).__init__()
        self.size = (width, height)
        self.color = color
        self.img = Image.new('RGB', (width, height), color=background_color)
        self.x, self.y = 0, 0
        self.age = 0

    def write_image(self, image_name):
        self.img.save(image_name)
