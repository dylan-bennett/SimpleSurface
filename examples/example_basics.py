#!/usr/bin/env python3
"""Examples of basic commands done using ImageSurfacePlus."""
import random

from PIL import ImageDraw
from PIL import ImageFont

from src.ImageSurfacePlus import ImageSurfacePlus


def random_rectangles(isp, num_rectangles):
    """Draw rectangles randomly all over the ImageSurfacePlus object."""
    for _ in range(num_rectangles):
        width = random.randint(0, isp.get_width() / 2)
        height = random.randint(0, isp.get_height() / 2)
        x = random.randint(0, isp.get_width() - width)
        y = random.randint(0, isp.get_height() - height)
        color = random.choices(range(256), k=4)
        isp.draw.rectangle(x, y, width, height, color=color)


# Create an ImageSurfacePlus object, sized 600x800 pixels
surface = ImageSurfacePlus(600, 800)

# Set the background to red
surface.set_background((255, 0, 0))

# Draw 10 rectangles randomly placed on it
random_rectangles(surface, 10)

# Crop it to a size 400x500 pixels, starting at (50, 50)
surface.crop(50, 50, 400, 500)

# Create a second ImageSurfacePlus object, sized 100x200 pixels
surface2 = ImageSurfacePlus(100, 200)

# Set the background to yellow
surface2.set_background((255, 255, 0))

# Draw 5 rectangles randomly placed on it
random_rectangles(surface2, 5)

# Outline it with a 5-pixel outline
surface2.outline(line_width=5)

# Paste it into the center of the first ImageSurfacePlus.
surface.paste(surface2, "center", "center")

# Draw gridlines on the first ImageSurfacePlus
# (outline, plus vertical/horizontal center lines)
surface.gridlines()

# Convert it to a PIL object
image = surface.to_pil()

# Write "Hello World" in black 25 pt font at (50, 50) using PIL commands
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("fonts/arial.ttf", 25)
draw.text((50, 50), "Hello World", (0, 0, 0), font=font)

# Convert the image back to an ImageSurfacePlus object
surface.from_pil(image)

# Save the result as a PNG file and a PDF file
surface.write_to_png("example_basics.png")
surface.write_to_pdf("example_basics.pdf")
