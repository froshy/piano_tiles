from ScreenGrabber import *
from ScreenShot import *

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
    grabber = ScreenGrabber(mon=2, output='dump.png', dim=dim)
    grabber.screenshot()


