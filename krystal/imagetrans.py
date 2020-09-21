from pathlib import Path
from enum import Enum
import numpy as np
import math as M


class CropDirection (Enum):
    """
    Crop directions defined
    """
    vert = 1
    hori = 2
    diag = 3


def batchcrop(path: Path, destDir: Path, targetSize=256, fileNameCallback=None):
    """
    Crop all images in a directory
    """


def cropimg(path: Path, destDir: Path, targetSize=256, fileNameCallback=None, cropModes=[CropDirection.vert, CropDirection.hori, CropDirection.diag]):
    """
    Crop one image
    """


def hcrop(im , t = 256, count = 3) :
    """
    Crops an image horizontally at the vertical center and returns the resulting 
    images.
    Input image should be of shape h, w, d or h, w
    Parameters
    ----------
    im : numpy.ndarray
        Format h, w, d or h, w
    t : int
        Target size
    count: int
        Target count. Using an odd number count gives the center
    Returns
    -------
    coords : numpy.ndarray (shape n x 2)
        Array of topleft coords
        Example: array([[  0, 125],
           [ 44, 125],
           [ 88, 125],
           [132, 125],
           [177, 125]])
    See Also
    --------
    vcrops, dcrops
    Examples
    --------
    >>> crops = ki.hcrop(im, t=128,count=7))
    >>> for n in crops:
    >>>     print(n)
    [  0 125]
    [ 44 125]
    [ 88 125]
    [132 125]
    [177 125]
    """
    h, w = im.shape[0], im.shape[1]
    toplimit = M.floor((h - t) / 2) # Same as h/2 - t/2
    lastp = w - t
    if lastp <= 0:
        raise Exception("Invalid crop size. Crop size is larger than image dimensions")
    xcuts = np.linspace(0, lastp, count).astype(int)
    xcuts  = xcuts[..., np.newaxis] # add new axis for appending
    tl = np.full(count, toplimit) # array of toplimit for appending
    tl = tl[..., np.newaxis] # add new axis for appending
    crops  = np.append(tl, xcuts, axis=1) # append to build top left coords
    return crops


def vcrop(im , t = 256, count = 3) :
    """
    Crops an image vertically at the horizontal center and returns the resulting 
    images.
    Input image should be of shape h, w, d or h, w
    Parameters
    ----------
    im : numpy.ndarray
        Format h, w, d or h, w
    t : int
        Target size
    count: int
        Target count. Using an odd number count gives the center
    Returns
    -------
    coords : numpy.ndarray (shape n x 2)
        Array of topleft coords
        Example: 
        array([[  0, 197],
       [ 88, 197],
       [177, 197]])
    See Also
    --------
    vcrops, dcrops
    Examples
    --------
    >>> crops = ki.vcrop(im, t=128,count=7))
    >>> for n in crops:
    >>>     print(n)
    """
    h, w = im.shape[0], im.shape[1]
    leftlimit = M.floor((w - t) / 2) # Same as h/2 - t/2
    lastp = h - t
    if lastp <= 0:
        raise Exception("Invalid crop size. Crop size is larger than image dimensions")
    ycuts = np.linspace(0, lastp, count).astype(int)
    ycuts  = ycuts[..., np.newaxis] # add new axis for appending
    tl = np.full(count, leftlimit) # array of leftlimit values for appending
    tl = tl[..., np.newaxis] # add new axis for appending
    crops  = np.append(ycuts, tl, axis=1) # append to build top left coords
    return crops


def imgcut(im, t, *crops):
    imlist = []
    for crop in crops:
        for c in crop:
            imlist.append(im[c[0]:c[0]+t, c[1]:c[1]+t])
    return imlist
