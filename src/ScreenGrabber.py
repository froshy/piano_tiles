import numpy as np
import logging
import mss


class ScreenGrabber:
    """
    Grabs a section of the screen/monitor. Should not change dimensions.
    To grab another part of the screen, instantiate a new ScreenGrabber object.
    """

    def __init__(self, mon=1, output='piano_tiles.png', **dim):
        """
        Parameters:
            mon (int): specifies which monitor to capture
            output (string): name of file of saved screenshot
            **dim (dict): diction specifying dimensions of screen capture, should be {'top': x, 'left': y, 'width': z,
                            'height': w}

        """
        self.mon = mon
        self.output = output
        self.dim = dim

    def screenshot(self) -> mss.ScreenShot:
        """
        Takes a screenshot with given self parameters
        """
        with mss.mss() as sct:
            monitor = sct.monitors[self.mon]
            sct_photo = sct.grab(monitor)
            return sct_photo


