from pathlib import Path
from enum import Enum
import numpy as np
import math as M


# def batchcrop(path: Path, destDir: Path, targetSize=256, fileNameCallback=None):
#     """
#     Crop all images in a directory
#     """


# def cropimg(path: Path, destDir: Path, targetSize=256, fileNameCallback=None, cropModes=[CropDirection.vert, CropDirection.hori, CropDirection.diag]):
#     """
#     Crop one image
#     """


def hcrop(im , t = 256, count = 3) :
    """
    Crops an image horizontally at the vertical center and returns the resulting 
    top left coords for cropping it later.
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
    if lastp < 0:
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
    top left coords for cropping it later.
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
    if lastp < 0:
        raise Exception("Invalid crop size. Crop size is larger than image dimensions")
    ycuts = np.linspace(0, lastp, count).astype(int)
    ycuts  = ycuts[..., np.newaxis] # add new axis for appending
    tl = np.full(count, leftlimit) # array of leftlimit values for appending
    tl = tl[..., np.newaxis] # add new axis for appending
    crops  = np.append(ycuts, tl, axis=1) # append to build top left coords
    return crops


def gridcrop(im, t = 256, crop_count = None):
    """
    Crops an image using a grid pattern and returns the resulting 
    top left coords for cropping it later.
    Input image should be of shape h, w, d or h, w
    Parameters
    ----------
    im : numpy.ndarray
        Format h, w, d or h, w
    t : int
        Target size
    crop_count: tuple (int, int) (optional)
        Optimal crop count is calculated based on image and target sizes and 
        used by default.
        Target count in the format (rows x cols) in the resulting grid. 
        Note: Using an odd number count gives the center.
    Returns
    -------
    coords : python array
        Array of topleft coords that can be used to generate crops
    See Also
    --------
    vcrop, hcrop
    Examples
    --------
   crg1 = kt.gridcrop(im, 128, (3, 5)) ; crg1
   [[0, 0],
     [0, 261],
     [0, 522],
     [76, 0],
     [76, 261],
     [76, 522],
     [152, 0],
     [152, 261],
     [152, 522],
     [228, 0],
     [228, 261],
     [228, 522],
     [305, 0],
     [305, 261],
     [305, 522]]
    
    Further slices from the result can give horizontal, vertical or diagonal strips from the grid
    >>>crg1[:3]
    [[0, 0], [0, 261], [0, 522]]
    >>>crg1[3*2:3*2+3] # Extract the middle row
    [152, 0], [152, 261], [152, 522]]
    >>>crg1[::5] # For a diagonal cut
    [[0, 0], [76, 522], [228, 261]]
    """
    # Optimal crop count is used by default if not provided
    crop_count = find_optimalcropcount(im, t) if crop_count is None else crop_count
    w, h = im.shape[1], im.shape[0]
    lastp_hor, lastp_vert = w -t, h - t
    
    if lastp_hor < 0 or lastp_vert < 0:
        raise Exception("Invalid crop size. Crop size is larger than image dimensions")
    
    xcuts = np.linspace(0, lastp_hor, crop_count[0]).astype(int)
    ycuts = np.linspace(0, lastp_vert, crop_count[1]).astype(int)
    
    crops = []
    for xi in ycuts:
        for yi in xcuts:
            crops.append([xi,yi])
    return crops, crop_count


def find_optimalcropcount(im, t = 256, trim_tolerance=0.2):
    """
    Optimal crop count for the grid crop is calculated based on image and target sizes.
    Parameters
    ----------
    im : numpy.ndarray
        Format h, w, d or h, w
    t : int
        Target size
    trim_ok : bool
        Determines whether trimming part of the image that does not exactly fit the crops is enabled
        Default is True
    Returns
    -------
    cropcount : tuple (int, int)
        optimal rows x cols for the grid crop
    """
    w, h = im.shape[1], im.shape[0]
    lastp_hor, lastp_vert = w -t, h - t
    
    if lastp_hor < 0 or lastp_vert < 0:
        raise Exception("Invalid crop size. Crop size is larger than image dimensions")
    
    # When trim_tolerance is 0.2,
    # if the last piece is less than 20% of target size it is left out
    x = M.floor(w / t) if (w % t) / t < trim_tolerance  else M.floor((w / t) + 1)
    y = M.floor(h / t) if (h % t) / t < trim_tolerance  else M.floor((h / t) + 1)
    return (x, y)
    

def imgcut(im, t, *cropslist):
    """
    Crops the input based on the list of crop top left coords.
    Input image should be of shape h, w, d or h, w
    Performance note: The result is a list of slices of the original image ndarray 
    and not memory copies.
    Parameters
    ----------
    im : numpy.ndarray
        Format h, w, d or h, w
    t : int
        Target size
        Use the same t here as used for the gridcrop.
    croplist: python list of ndarrays
        List of crop top left coords.
    Returns
    -------
    imlist : List of cropped images in the same format as input image
    See Also
    --------
    gridcrop
    Examples
    --------
    >>> crops = ki.vcrop(im, t=128,count=7))
    >>> for n in crops:
    >>>     print(n)
    """
    imlist = []
    for crop in cropslist:
        for c in crop:
            imlist.append(im[c[0]:c[0]+t, c[1]:c[1]+t])
    return imlist
