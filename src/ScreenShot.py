import mss
import cv2
import os


class ScreenShot:
    """
    Essentially a wrapper for ScreenShot class from mss
    """

    def __init__(self, sc: mss.base.ScreenShot, output):
        self.sc = sc
        self.save_path = output

    def rgb(self):
        return self.sc.pixels

    def pixel(self, x, y):
        return self.sc.pixel(x, y)

    def save_png(self, overwrite=True):
        """
        output: string name of output file (ends in .png)

        """
        if not os.path.isfile(self.save_path) or overwrite:
            mss.tools.to_png(self.sc.rgb, self.sc.size, output=self.save_path)
        else:
            counter = 1

            stem = self.save_path.stem
            new_fname = self.save_path
            while os.path.isfile(new_fname):
                new_fname = self.save_path.with_stem(f'{stem}{counter}')
                counter += 1
            mss.tools.to_png(self.sc.rgb, self.sc.size, output=new_fname)


