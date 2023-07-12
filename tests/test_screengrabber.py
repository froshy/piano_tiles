from src.ScreenGrabber import *
import mss
import logging
import os
import pathlib
import pytest


def test_screenshot():

    logging.info(f'Started Test screenshot')

    grabber = ScreenGrabber(mon=2)
    rgb = grabber.screenshot()

    assert grabber

    logging.info(f'Ended Test screenshot')


def test_partial_screenshot():
    sct_height = 100
    sct_width = 595

    sct_top = 500
    sct_left = 665

    monitor = 2
    dim = {
        'top': sct_top,
        'left': sct_left,
        'height': sct_height,
        'width': sct_width
    }
    output_folder = pathlib.Path('/home/froshy/piano_tiles/screenshot_dump')
    os.makedirs(output_folder, exist_ok=True)
    grabber = ScreenGrabber(mon=2, save_path=output_folder, sct_file='test.png', dim_dict=dim)
    sct_photo = grabber.screenshot()
    sct_photo.save_png(overwrite=True)


