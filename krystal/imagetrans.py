import cv2
from pathlib import Path

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


def batchCropImages(path: Path, destPath: Path, ):
    """
    Crop all images in a directory
    """
