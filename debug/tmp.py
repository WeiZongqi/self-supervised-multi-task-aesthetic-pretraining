import cv2 as cv
from PIL import Image
import numpy as np

img = cv.imread('/Users/bytedance/show/show0630/tmp0630/tmp/地名地址信息_自然地名_b4a9f0c02ab70f4f03fb517cd7880c35-inpaint_0.jpg')
hist = cv.calcHist([img], [0], None, [256], [0, 256])
hist = np.squeeze(hist)
hist = hist[1:]
hist = (hist - min(hist)) / (max(hist) - min(hist))
print(hist)