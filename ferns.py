from PIL import Image, ImageDraw
import random

class BarnsleyFern(object):
    def __init__(self, width, height, color='black', background_color='white'):
        super(BarnsleyFern, self).__init__()
        self.size = (width, height)
        self.color = color
        self.height = height
        self.width = width
        self.border = 30
        self.img = Image.new('RGB', (width, height), color=background_color)
        self.age = 0
        self.points = []

    def write_image(self, image_name):
        self.img.save(image_name)

    def draw_points(self):
        for point in self.points:
            ImageDraw.Draw(self.img).point(point,fill="black")

    def scale(self, x, y):
        scale = 1.25
        x_offset = self.width/4
        y_offset = 1000
        h = ((x + 2.182)*(self.width - 1)/4.8378) / (1.75 * scale)
        k = (9.9983 - y)*(self.height - 1)/9.9983 / (scale)
        return h + x_offset, k + y_offset

    def transform(self, x, y):
        rand = random.uniform(0, 100)
        if rand < 1:
            return 0, 0.16*y
        elif 1 <= rand < 86:
            return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
        elif 86 <= rand < 93:
            return 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6
        else:
            return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44

    def iterate(self, iterations):
        x = 0 + self.border / 2
        y = 0 + self.border / 2
        for _ in range(iterations):
            self.points.append(self.scale(x, y))
            x, y = self.transform(x, y)

# Iterations = shading
