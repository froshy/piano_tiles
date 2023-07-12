import numpy as np
import logging
from pathlib import *
from src import ScreenShot
from src.ScreenGrabberConfig import ScreenGrabberConfig
import mss





class ScreenGrabber:
    """
    Grabs a section of the screen/monitor. Should not change dimensions.
    To grab another part of the screen, instantiate a new ScreenGrabber object.
    """

    def __init__(self, dim_dict=None, mon=1, sct_file='piano_tiles.png', save_path=None):
        """
        Parameters:
            mon (int): specifies which monitor to capture
            output (string): name of file of saved screenshot
            dim_dict (dictionary): in format of
                                {
                                'top' : x,
                                'left' : y,
                                'width' : z,
                                'height' : w
                                }
        """
        self.config = ScreenGrabberConfig(mon, sct_file, dim_dict, save_path)
        self.mss_f = mss.mss
        self.mon = mon
        self.dim = self.config.dim

    def screenshot(self) -> ScreenShot.ScreenShot:
        """
        Takes a screenshot with given self parameters
        """
        with self.mss_f() as sct:

            monitor = self._screenshot_set_monitor(sct)
            sct_photo = sct.grab(monitor)
            return ScreenShot.ScreenShot(sct_photo, self.config.save_path)

    def _screenshot_set_monitor(self, sct):
        """
        Sets the monitor properly if a dimension is passed. Else, it is set to take entire monitor screen.
        """
        if self.dim:
            monitor = self.dim
        else:
            monitor = sct.monitors[self.mon]
        return monitor

