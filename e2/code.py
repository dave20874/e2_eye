# SPDX-FileCopyrightText: 2023 David Wheeler
# SPDX-License-Identifier: MIT

"""
This code will initialize the display using displayio and draw graphic elements to
look like the E2 droid's eye.
"""
import time

import displayio
import terminalio
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo
from adafruit_display_shapes.circle import Circle

# Create the TFT Gizmo display
display = tft_gizmo.TFT_Gizmo()

# Make the display context
splash = displayio.Group()
display.show(splash)

# Black background.
color_bitmap = displayio.Bitmap(240, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000  # Black background
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw iris
iris_color = 0xFFc000  # 0xFFC000 is pretty close.
iris = Circle(120, 120, 120, fill=iris_color, outline=iris_color)
splash.append(iris)

# Draw black pupil
pupil = Circle(120, 120, 90, fill=0x000000, outline=0x000000)
pupil_sprite = displayio.TileGrid(pupil.bitmap, pixel_shader=pupil.pixel_shader, x=30, y=30)
splash.append(pupil_sprite)

# Draw highlight
highlight_color = 0xC09000
highlight = Circle(10, 10, 20, fill=highlight_color, outline=highlight_color)
# highlight_palette = displayio.Palette(2)
# highlight_palette[0] = highlight_color
# highlight_palette[1] = highlight_color

highlight_sprite = displayio.TileGrid(highlight.bitmap, pixel_shader=highlight.pixel_shader, x=120, y=120)
splash.append(highlight_sprite)

while True:
    highlight_sprite.x = 130
    pupil_sprite.x = 40
    display.show(splash)
    time.sleep(1)
    highlight_sprite.x = 120
    pupil_sprite.x = 30
    display.show(splash)
    time.sleep(1)

