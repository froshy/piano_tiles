import mss


class Screenshot:
    """
    Essentially a wrapper for ScreenShot class from mss
    """

    def __init__(self, sc: mss.ScreenShot):
        self.sc = sc

    def rgb(self):

        return self.sc.pixels
