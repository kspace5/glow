import cv2
from pathlib import Path
from matplotlib import pyplot as plt
from . import utils
# from IPython.display import Video
# from IPython.display import HTML


def imread(path: Path):
    """
    Read the image from the Path as a numpy array
    Parameters
    ----------
    p : Path
        Image path
    Returns
    -------
    img : numpy.ndarray
        Image data in the format (h x w x d) or (h x w)
    See Also
    --------
    imshow
    Examples
    --------
    >>>imread(bpath / "mushrooms.jpg")
    """
    img =  cv2.imread(str(path))
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

load = imread

def imwrite(path: Path, im):
    """
    Writes the image to the Path as an image
    Parameters
    ----------
    p : Path
        Image path
    im : image data - numpy.ndarray
    Returns
    -------
    NIL
    See Also
    --------
    imshow, imread
    Examples
    --------
    >>>imwrite(bpath / "mushrooms.jpg", im)
    """
    im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
    cv2.imwrite(str(path), im)
    
save = imwrite

def imshow(img, title="Image"):
    """
    Display the image. img should be in ndarray format
    Parameters
    ----------
    p : Path
        Image path
    title: string
        Optional title
    Returns
    -------
    None
    See Also
    --------
    imread
    Examples
    --------
    >>>imread(bpath / "mushrooms.jpg")
    """
    if utils.is_notebook():
        plt.imshow(img)
        plt.title(title)
        plt.show()
    else:
        cv2.imshow(title, img)
        
show = imshow

def imgrid(imlist, rows, cols, size=30):
    """
    Display images in a grid. Maximum number of images is limited to the rows*cols
    or the imlist size, which ever is smaller.
    Parameters
    ----------
    imlist:
        python list of images in nd.array format
    rows, cols: int
        Grid rows and cols
    size: desired size of each image
        Converted to Matplotlib grid figure size in inches based on grid size
    Returns
    -------
    None
    See Also
    --------
    imshow, imread
    Examples
    --------
    >>>kim.imgrid(imlist, 5, 5, 30
    >>>kim.imgrid(imlist[2:6], 2, 3, 30)
    """
    fig = plt.figure(figsize=(int(size*rows/10), int(size*cols/10)))
    subplots = []
    L = cols * rows
    gsize = L if L < len(imlist) else len(imlist)
    for i in range(gsize):
        img = imlist[i]
        # create subplots and append plt
        subplots.append( fig.add_subplot(cols, rows, i+1) )
        subplots[-1].set_title("im:"+str(i))  # set title
        plt.imshow(img)
    plt.show()

grid = imgrid
    
    
# def vidshow(vidPath):
#     """Display a video from a given path (string)"""
# #     if utils.is_notebook():
# #        Video(str(vidPath))
#     HTML("""
#         <h1>Test<h1>
#         <video alt="test" controls>
#             <source src="{}" type="video/mp4">
#         </video>
#     """.format(str(vidPath)))
# #     else:
# #         raise Exception("Only supported in notebook mode")