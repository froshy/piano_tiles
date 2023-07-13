from src.ScreenGrabber import *
from src.util import *
import time

"""
Drives the application. Only works on primary monitor
"""
def driver():
    sct_height = 100
    sct_width = 595

    sct_top = 500
    sct_left = 665

    monitor = 2
    output_folder = '/home/froshy/piano_tiles/screenshot_dump'
    dim = {
        'top': sct_top,
        'left': sct_left,
        'height': sct_height,
        'width': sct_width
    }
    grabber = ScreenGrabber(mon=2, dim_dict=dim)

    while True:
        sct = grabber.screenshot()
        check, x, y = sct.is_line_black(50)
        if check:
            move_and_click(x, y, grabber.config)
            print('clicked')


driver()




