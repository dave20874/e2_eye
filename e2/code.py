# SPDX-FileCopyrightText: 2023 David Wheeler
# SPDX-License-Identifier: MIT

"""
This code will initialize the display using displayio and draw graphic elements to
look like the E2 droid's eye.
"""
import time
import board

import displayio
from adafruit_gizmo import tft_gizmo
import adafruit_imageload
import neopixel

RED = (255, 0, 0)


class E2_Eye:
    def __init__(self):
        #
        # self.backlight = DigitalInOut(board.A3)
        # self.backlight.direction = OUTPUT
        # self.backlight.value = True

        # self.pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)
        # self.pixels.fill(RED)
        # self.pixels.show()

        # Create the TFT Gizmo display
        self.display = tft_gizmo.TFT_Gizmo()
        self.load_image(1)


        """
        # Black background.
        color_bitmap = displayio.Bitmap(240, 240, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = 0x000000  # Black background
        self.bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
        self.splash.append(self.bg_sprite)

        # Draw iris
        iris_color = 0xFFc000  # 0xFFC000 is pretty close.
        iris = Circle(120, 120, 120, fill=iris_color, outline=iris_color)
        self.iris_sprite = displayio.TileGrid(iris.bitmap, pixel_shader=iris.pixel_shader, x=0, y=0)
        self.splash.append(self.iris_sprite)

        # Draw black pupil
        pupil = Circle(120, 120, 90, fill=0x000000, outline=0x000000)
        self.pupil_sprite = displayio.TileGrid(pupil.bitmap, pixel_shader=pupil.pixel_shader, x=30, y=30)
        self.splash.append(self.pupil_sprite)

        # Draw highlight
        highlight_color = 0xC09000
        highlight = Circle(10, 10, 20, fill=highlight_color, outline=highlight_color)
        # highlight_palette = displayio.Palette(2)
        # highlight_palette[0] = highlight_color
        # highlight_palette[1] = highlight_color

        self.highlight_sprite = displayio.TileGrid(highlight.bitmap, pixel_shader=highlight.pixel_shader, x=120, y=120)
        self.splash.append(self.highlight_sprite)
        """

        self.update_interval = 3.0
        self.t = time.time()
        self.index = 0

    def load_image(self, n):
        filename = f"images/image{n}.PNG"

        # Make the display context
        self.main_group = displayio.Group(scale=2)


        image, palette = adafruit_imageload.load(
            filename, bitmap=displayio.Bitmap, palette=displayio.Palette
            )
        self.tile_grid = displayio.TileGrid(image, pixel_shader=palette,
                                            tile_width=120,
                                            tile_height=120)
        self.main_group.append(self.tile_grid)
        self.display.root_group = self.main_group


    def service(self):
        now = time.time()
        elapsed = now - self.t

        if elapsed >= self.update_interval:

            
            # switch the image
            self.index += 1
            if self.index >= 21:
                self.index = 0
            self.load_image(self.index)
            self.t = now


            
            
eye = E2_Eye()

while True:
    eye.service()


