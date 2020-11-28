# krystal
Image Processing for Deep Learning

## Install instructions
From conda or any python env  
pip install git+https://github.com/krexspace/krystal.git  

Depends on cv2, pathlib etc  

## Sample Usage
from pathlib import Path  
bpath  = Path("../data") ; bpath  

import krystal as kr  
im  = kr.imread(bpath / "images1" / "mushrooms.jpg")  
kr.imshow(im)  
