# GLOW
Image Processing for Deep Learning

## Install instructions
From conda or any python env  
pip install git+https://github.com/krexspace/glow.git

Depends on cv2, pathlib etc  

## Sample Usage
from pathlib import Path  
bpath  = Path("../data") ; bpath  

import glow as gl  
im  = gl.imread(bpath / "images1" / "mushrooms.jpg")  
gl.imshow(im) 

