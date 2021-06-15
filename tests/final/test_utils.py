import glow.utils as gu
from pathlib import Path

flist = gu.filePathList(Path("../temp_del/frames2"))
print(flist)

flist = gu.fileNameList(Path("../temp_del/frames"), "img??.png")
print(flist)

flist = gu.fileNameList(Path("../temp_del/frames"), "img*.*")
print(flist)
