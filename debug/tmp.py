import cv2 as cv
from PIL import Image
import numpy as np
import random


def getHist():
    img = cv.imread('/Users/bytedance/show/show0630/tmp0630/tmp/地名地址信息_自然地名_b4a9f0c02ab70f4f03fb517cd7880c35-inpaint_0.jpg')
    hist = cv.calcHist([img], [0], None, [256], [0, 256])
    hist = np.squeeze(hist)
    hist = hist[1:]
    hist = (hist - min(hist)) / (max(hist) - min(hist))
    print(hist)


def mkAug0():
    img = cv.imread(
        '/Users/bytedance/show/show0630/tmp0630/tmp/地名地址信息_自然地名_b4a9f0c02ab70f4f03fb517cd7880c35-inpaint_0.jpg')
    print(img.shape)

    h, w, c= img.shape

    def _crop_img(img, box):
        x1, y1, x2, y2 = box
        return img[y1:y2, x1:x2, :]

    radio = 0.85
    vertical = img[::-1, :, :]
    a_h = int(random.random() * (1 - radio) * h)
    a_w = int(random.random() * (1 - radio) * w)

    a_h = int(h * 0.08)
    a_w = int(w * 0.08)

    print(h, a_h, w, a_w, '+++')

    crop1 = _crop_img(img, [a_w, a_h, int(a_w + radio * w), int(a_h + radio * h)])


    # print(h,w,c)
    cv.imshow('test',img)
    cv.imshow('vertical',vertical)
    cv.imshow('crop',crop1)

    cv.waitKey()
mkAug0()