import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def process(filename: str=None) -> None:
    """
    View multiple images stored in files, stacking vertically

    Arguments:
        filename: str - path to filename containing image
    """
    image = mpimg.imread(filename)
    # <something gets done here>
    plt.figure()
    plt.imshow(image)

intitial_img_address = 'drive/MyDrive/killer.jpeg'
img = Image.open(intitial_img_address)

text = 'THE KILLER'
# font = ImageFont.truetype(font='arial.ttf', size=25)
color = (255, 0, 0)
starting_point = (35, 50)

draw = ImageDraw.Draw(img)
draw.text(xy=starting_point, text=text, fill=color)

# img.show()

saved_img_address = 'drive/MyDrive/THE_KILLER.jpeg'

img.save(saved_img_address)


img_address = [intitial_img_address, saved_img_address]

for img in img_address:
    process(img)