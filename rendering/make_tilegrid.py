from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from PIL.Image import Palette
import math



# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GREY = (20, 20, 20)
IRIS_GLOW = (255, 0, 0)
IRIS_GLARE = (255, 220, 220)
PUPIL_COLOR = BLACK
BACKING_COLOR = DARK_GREY
CENTER_COLOR = IRIS_GLOW

#sizes
IRIS_RADIUS = 60
PUPIL_RADIUS = 45
BACKING_RADIUS = 62
CENTER_RADIUS = 10

#depths
BACKING_DEPTH = 30
IRIS_DEPTH = 40
CENTER_DEPTH = 15

"""
dark_grey = (20, 20, 20)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (0, 128, 128)
colors = [red, green, blue, yellow]
"""



# Draw the eye's components into an image via drawing context draw.
# The eye's direction is defined by first pitching down by -pitch, then rolling by roll.
def draw_eye(pitch, roll):
    # Create a working image to draw in.  We'll copy this to input draw context at the end.
    im2 = Image.new("RGB", [240, 240], BLACK)
    cx = 120
    cy = 120
    d2 = ImageDraw.Draw(im2)

    # In this section, the convention is Y+ is up, (0, 0) is center of eye when neutral
    # I'll map these to image coords after doing the mathy part


    # Iris Backing
    y_offset = BACKING_DEPTH * math.sin(pitch)
    y_top = BACKING_RADIUS * math.cos(pitch) + y_offset
    y_bottom = -BACKING_RADIUS * math.cos(pitch) + y_offset

    x_left = -BACKING_RADIUS
    x_right = BACKING_RADIUS

    # Now convert to image coordinates
    x1 = int(cx + x_left)
    x2 = int(cx + x_right)
    y1 = int(cy - y_top)
    y2 = int(cy - y_bottom)
    bounds = (x1, y1, x2, y2)

    # Draw the ellipse in the temp image
    # print(f"bounds: {x1}, {y1}, {x2}, {y2}")
    d2.ellipse(bounds, outline=BLACK, fill=BACKING_COLOR)


    # Iris
    y_offset = IRIS_DEPTH * math.sin(pitch)
    y_top = IRIS_RADIUS * math.cos(pitch) + y_offset
    y_bottom = -IRIS_RADIUS * math.cos(pitch) + y_offset

    x_left = -IRIS_RADIUS
    x_right = IRIS_RADIUS

    # Now convert to image coordinates
    x1 = int(cx + x_left)
    x2 = int(cx + x_right)
    y1 = int(cy - y_top)
    y2 = int(cy - y_bottom)
    bounds = (x1, y1, x2, y2)

    # Pupil
    y_offset = IRIS_DEPTH * math.sin(pitch)
    y_top = PUPIL_RADIUS * math.cos(pitch) + y_offset
    y_bottom = -PUPIL_RADIUS * math.cos(pitch) + y_offset

    x_left = -PUPIL_RADIUS
    x_right = PUPIL_RADIUS

    # Now convert to image coordinates
    x1 = int(cx + x_left)
    x2 = int(cx + x_right)
    y1 = int(cy - y_top)
    y2 = int(cy - y_bottom)
    bounds = (x1, y1, x2, y2)

    # Draw the ellipse in the temp image
    # print(f"bounds: {x1}, {y1}, {x2}, {y2}")
    d2.ellipse(bounds, outline=BLACK, fill=PUPIL_COLOR)

    # Center
    y_offset = CENTER_DEPTH * math.sin(pitch)
    y_top = CENTER_RADIUS * math.cos(pitch) + y_offset
    y_bottom = -CENTER_RADIUS * math.cos(pitch) + y_offset

    x_left = -CENTER_RADIUS
    x_right = CENTER_RADIUS

    # Now convert to image coordinates
    x1 = int(cx + x_left)
    x2 = int(cx + x_right)
    y1 = int(cy - y_top)
    y2 = int(cy - y_bottom)
    bounds = (x1, y1, x2, y2)

    # Draw the ellipse in the temp image
    # print(f"bounds: {x1}, {y1}, {x2}, {y2}")
    d2.ellipse(bounds, outline=BLACK, fill=CENTER_COLOR)

    # Copy center of the image to the destination
    # im2.show()
    im_rotate = im2.rotate(math.degrees(roll), resample=Image.BICUBIC)
    crop = im_rotate.crop((60, 60, 180, 180))
    # crop.show()

    return crop

def draw_eye_components(pitch, roll, iris_color):
    # Create a working image to draw in.  We'll copy this to input draw context at the end.
    im2 = Image.new("RGBA", [240, 240], (0, 0, 0, 0))
    cx = 120
    cy = 120
    d2 = ImageDraw.Draw(im2)

    # In this section, the convention is Y+ is up, (0, 0) is center of eye when neutral
    # I'll map these to image coords after doing the mathy part

    # Iris
    y_offset = IRIS_DEPTH * math.sin(pitch)
    y_top = IRIS_RADIUS * math.cos(pitch) + y_offset
    y_bottom = -IRIS_RADIUS * math.cos(pitch) + y_offset

    x_left = -IRIS_RADIUS
    x_right = IRIS_RADIUS

    # Now convert to image coordinates
    x1 = int(cx + x_left)
    x2 = int(cx + x_right)
    y1 = int(cy - y_top)
    y2 = int(cy - y_bottom)
    bounds = (x1, y1, x2, y2)

    # Draw the ellipse in the temp image
    # print(f"bounds: {x1}, {y1}, {x2}, {y2}")
    d2.ellipse(bounds, outline=iris_color, fill=iris_color)

    # Pupil
    y_offset = IRIS_DEPTH * math.sin(pitch)
    y_top = PUPIL_RADIUS * math.cos(pitch) + y_offset
    y_bottom = -PUPIL_RADIUS * math.cos(pitch) + y_offset

    x_left = -PUPIL_RADIUS
    x_right = PUPIL_RADIUS

    # Now convert to image coordinates
    x1 = int(cx + x_left)
    x2 = int(cx + x_right)
    y1 = int(cy - y_top)
    y2 = int(cy - y_bottom)
    bounds = (x1, y1, x2, y2)

    # Draw the ellipse in the temp image
    # print(f"bounds: {x1}, {y1}, {x2}, {y2}")
    d2.ellipse(bounds, outline=(0, 0, 0, 0), fill=(0, 0, 0, 0))

    # Center
    y_offset = CENTER_DEPTH * math.sin(pitch)
    y_top = CENTER_RADIUS * math.cos(pitch) + y_offset
    y_bottom = -CENTER_RADIUS * math.cos(pitch) + y_offset

    x_left = -CENTER_RADIUS
    x_right = CENTER_RADIUS

    # Now convert to image coordinates
    x1 = int(cx + x_left)
    x2 = int(cx + x_right)
    y1 = int(cy - y_top)
    y2 = int(cy - y_bottom)
    bounds = (x1, y1, x2, y2)

    # Draw the ellipse in the temp image
    # print(f"bounds: {x1}, {y1}, {x2}, {y2}")
    d2.ellipse(bounds, outline=iris_color, fill=iris_color)

    # Copy center of the image to the destination
    # im2.show()
    im_rotate = im2.rotate(math.degrees(roll), resample=Image.BICUBIC)

    return im_rotate

# Draw the eye's components into an image via drawing context draw.
# The eye's direction is defined by first pitching down by -pitch, then rolling by roll.
def draw_eye2(pitch, roll):

    big_blur = ImageFilter.GaussianBlur(radius=8)
    small_blur = ImageFilter.GaussianBlur(radius=1.0)


    base_im = Image.new("RGB", (240, 240), (0, 0, 0))
    glow = draw_eye_components(pitch, roll, IRIS_GLOW)
    glow = glow.filter(big_blur)
    brighten = ImageEnhance.Brightness(glow)
    glow = brighten.enhance(2.0)
    
    overexposed = draw_eye_components(pitch, roll, IRIS_GLARE)
    overexposed = overexposed.filter(small_blur)

    base_im.paste(glow)
    base_im.paste(overexposed, mask=overexposed)

    crop = base_im.crop((60, 60, 180, 180))

    return crop


pitches = [0.0, -15.0, -30.0]
rolls = [-120.0, -90.0, -60.0, 0.0, 60.0, 90.0, 120.0]

n = 0
for pitch in pitches:
    for roll in rolls:
        img = draw_eye2(math.radians(pitch), math.radians(roll))

        # Save this image as a PNG
        p_image = img.convert("P", palette=Palette.ADAPTIVE)
        p_image.save(f"images/image{n}.PNG", optimize=True)

        n += 1
