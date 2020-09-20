import cv2
from pathlib import Path
from enum import Enum
from . import utils
# # load the input image and show its dimensions, keeping in mind that
# # images are represented as a multi-dimensional NumPy array with
# # shape no. rows (height) x no. columns (width) x no. channels (depth)
# imPath = Path(Path.cwd())
# imPath /= "temp/frame100.png"
# print(imPath)
# image = cv2.imread(str(imPath))
# (h, w, d) = image.shape
# print("width={}, height={}, depth={}".format(w, h, d))
# print(type(image))
# # cv2.imshow("Image R", image[:,:,0])
# # cv2.imshow("Image G", image[:,:,1])
# # cv2.imshow("Image B", image[:,:,2])
# mxy = 400
# cv2.imshow("Image Cropped0", image[0:mxy,0:mxy,:])
# cv2.imshow("Image Cropped1", image[0:mxy,-mxy:,:])
# cv2.imshow("Image Cropped2", image[-mxy:,0:mxy,:])
# cv2.imshow("Image Cropped3", image[-mxy:,-mxy:,:])
# cv2.waitKey(0)


class CropDirection (Enum):
    """
    Crop directions defined
    """
    vert = 1
    hori = 2
    diag = 3


def batchCropImages(path: Path, destDir: Path, targetSize=256, fileNameCallback=None):
    """
    Crop all images in a directory
    """


def cropImage(path: Path, destDir: Path, targetSize=256, fileNameCallback=None, cropModes=[CropDirection.vert, CropDirection.hori, CropDirection.diag]):
    """
    Crop one image
    """


# image should be of shape w, h, d
def crop_d1(path: Path, ):
    """

    """
    return False