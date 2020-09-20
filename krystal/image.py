import cv2
from pathlib import Path
from matplotlib import pyplot as plt
from . import utils


def imread(path: Path):
    """Read the image from the Path as a numpy array"""
    img =  cv2.imread(str(path))
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def imshow(img, title="Image"):
    """Display the image. img should be in ndarray format"""
    if utils.is_notebook():
        plt.imshow(img)
        plt.title(title)
        plt.show()
    else:
        cv2.imshow(title, img)