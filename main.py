from ferns import BarnsleyFern

fern_example = BarnsleyFern(10000, 10000, "white", "white")

fern_example.iterate(10000000)
fern_example.draw_points()
fern_example.write_image('test.png')