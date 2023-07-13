import pyautogui
import time


def move_and_click(x,y, config):

    x_adj, y_adj = adjust_coord(x, y, config)
    pyautogui.moveTo(x_adj, y_adj)
    time.sleep(.05)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()


def adjust_coord(x, y, config):
    """
    x, y are coords relative to screenshot,

    Used for pyautogui functions
    Return x_adj, y_adj, coords relative to monitor
    """

    from_top = config.dim['top']
    from_left = config.dim['left']

    x_adj = x + from_left
    y_adj = y + from_top

    return x_adj, y_adj
