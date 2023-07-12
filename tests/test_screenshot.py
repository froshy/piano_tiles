"""
Testing module for ScreenShot.py
"""
import pytest
import os
from src import ScreenGrabber
from pathlib import *


@pytest.fixture
def grabber():
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
    output_folder = Path('/home/froshy/piano_tiles/screenshot_dump')
    os.makedirs(output_folder, exist_ok=True)
    grabber = ScreenGrabber.ScreenGrabber(mon=2, save_path=output_folder, sct_file='test.png', dim_dict=dim)
    return grabber


def test_multiple_screenshot(grabber):
    grabber = grabber
    screenshot = grabber.screenshot()

    for i in range(50):
        screenshot.save_png(overwrite=False)
