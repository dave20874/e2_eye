# SPDX-FileCopyrightText: 2023 David Wheeler
# SPDX-License-Identifier: MIT

"""
This code will initialize the display using displayio and draw graphic elements to
look like the E2 droid's eye.
"""
import time
import board
from digitalio import DigitalInOut, Direction, Pull

import displayio
import terminalio
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo
from adafruit_display_shapes.circle import Circle


class E2_Eye:
    def __init__(self):
        #
        # self.backlight = DigitalInOut(board.A3)
        # self.backlight.direction = OUTPUT
        # self.backlight.value = True

        # Create the TFT Gizmo display
        self.display = tft_gizmo.TFT_Gizmo()

        # Make the display context
        self.splash = displayio.Group()
        self.display.root_group = self.splash

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

        self.direction = 1
        self.distance = 10
        self.update_interval = 2.0
        self.t = time.time()

    def service(self):
        now = time.time()
        elapsed = now - self.t

        if elapsed >= self.update_interval:
            self.highlight_sprite.x += self.distance * self.direction
            if self.direction > 0:
                self.display.brightness = 0.5
            else:
                self.display.brightness = 1.0
            self.direction *= -1
            self.t = now
            
            
eye = E2_Eye()

while True:
    eye.service()


