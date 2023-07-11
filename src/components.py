import numpy as np
import logging
import mss


class ScreenGrabber:

    def __init__(self, mon=1, output='piano_tiles.png', **dim):
        self.mon = mon
        self.output = output
        self.dim = dim

    def screenshot(self) -> mss.ScreenShot:
        with mss.mss() as sct:
            monitor = sct.monitors[self.mon]
            sct_photo = sct.grab(monitor)
            return sct_photo.pixels
            png = mss.tools.to_png(sct_photo.rgb, sct_photo.size)
            return sct_photo.rgb
