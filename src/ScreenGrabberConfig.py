"""
Module for the screengrabber config. Should be set up here
"""

from pathlib import *
import mss


def initialize_dim(dim_dict, monitor_num, mss_f):
    """
    dim is in the format:
    {
    'top': x,
    'left': y,
    'width': z,
    'height': w
    }
    returns an initialized dim for taking screenshot another monitor
    """
    if dim_dict:
        with mss_f() as sct:
            mon = sct.monitors[monitor_num]
            dim_dict['top'] += mon['top']
            dim_dict['left'] += mon['left']
            dim_dict['mon'] = monitor_num
        return dim_dict
    return


class ScreenGrabberConfig:
    """
    Config object has the following parameters:

    self.mon
    self.save_path (complete output path including .png)
    self.dim
    """

    def __init__(self, mon, sct_file, dim_dict, folder_save_path):
        self.mon = mon
        if not folder_save_path:
            folder_save_path = Path('home/froshy/piano_tiles/screenshot_dump')
        self.save_path = folder_save_path / sct_file
        self.dim = initialize_dim(dim_dict, mon, mss.mss)
        self.sct_file = sct_file
        self.folder_save_path = folder_save_path
