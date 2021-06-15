# Video util functions
import cv2
from pathlib import Path


def extractFrames(videoFilePath, destPath, frameNamePattern="frame{}.png", extractDelta=30, maxFrames=-1, frameStart=0):
    """
    Extracts video frames to images
        Non-scalar `start` and `stop` are now supported.
    Parameters
    ----------
    videoFilePath : Path
        Full path to video file 
    destPath : Path
        Path to extract image frames. Creates the dest dir and all parents if not exists
    frameNamePattern: string
        Pattern for frame image file naming. Example: "frame{}.png".format(frameCount)
    extractDelta : int, optional
        Frame stride
    maxFrames : int, optional
        Maximum frames to extract (Not implemented yet)
    frameStart : int, optional
        Start with frame (Not implemented yet)
    Returns
    -------
    frameCount : int
        Total frames read
    extractCount : int, optional
        Total frames extracted
    See Also
    --------
    Examples
    --------
    >>> result = kv.extractFrames("../temp_del/movx1.mp4", destPath="../temp_del/frames")
    (1605, 54)
    >>> np.linspace(2.0, 3.0, num=5, endpoint=False)
    array([2. ,  2.2,  2.4,  2.6,  2.8])
    >>> plt.show()
    """
    # Path to video file
    vidObj = cv2.VideoCapture(str(videoFilePath))
    # Used as counter variable
    frameCount = 0
    extractCount = 0
    # checks whether frames were extracted
    success = True
    # creates the dest dir and all parents if not exists
    destPath.mkdir(parents=True, exist_ok=True)
    while success:
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        # Saves the frames with frame-count
        if success:
            if frameCount % extractDelta == 0:
                extractCount += 1
                cv2.imwrite(str(destPath) + "/" + frameNamePattern.format(frameCount), image)
        else:
            # print("Extracted {} frames out of {}".format(extractCount, frameCount))
            break
        frameCount += 1

    vidObj.release()
    return frameCount, extractCount


# Driver Code
if __name__ == '__main__':
    # Calling the function
    extractFrames("/mnt/arkx/203_SEASON_DEEPLEARNING/image_proc_starter/temp_del/movx1.mp4")
