from src.components import *
import logging
import pytest


def test_screenshot():

    logging.info(f'Started Test screenshot')

    grabber = ScreenGrabber(mon=2)
    rgb = grabber.screenshot()

    assert grabber

    logging.info(f'Ended Test screenshot')
