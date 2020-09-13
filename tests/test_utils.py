import krystal.utils as ku
from pathlib import Path

flist = ku.filePathList(Path("../temp_del/frames2"))
print(flist)

flist = ku.fileNameList(Path("../temp_del/frames"), "img??.png")
print(flist)

flist = ku.fileNameList(Path("../temp_del/frames"), "img*.*")
print(flist)
