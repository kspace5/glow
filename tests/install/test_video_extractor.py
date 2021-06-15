import krystal.video as kv

result = kv.extractFrames("../temp_del/movx1.mp4", destPath="../temp_del/frames", extractDelta=5, frameNamePattern="img{}.png")
print(result)

