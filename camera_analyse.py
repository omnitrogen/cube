import math
import time
import os
import cv2
import numpy as np
import imutils

from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import ast

import settings
from nearest_color import ColorNames

from goprocam import GoProCamera
from goprocam import constants


class Camera(GoProCamera.GoPro):
    """ GoPro class """

    def __init__(self):
        """ Class initialiser """
        GoProCamera.GoPro.__init__(self, constants.gpcontrol)
        self.path = str()

    def take_photo(self):
        """ take pic, download it and return the path of the pic """
        time.sleep(0.5)
        GoProCamera.GoPro.take_photo(self)
        GoProCamera.GoPro.downloadLastMedia(self)
        self.path = os.getcwd() + "/" + "118GOPRO-" + str(self.getMediaInfo("file"))


def analyse_pic():
    """ analyse the cube and return 9 colors (one for each cube on a face) """

    def approximate_lum(imageApprox):
        """approximation of luminosity in the pic"""
        sb, sg, sr = 0, 0, 0
        for i in range(imageApprox.shape[0]):
            for j in range(imageApprox.shape[1]):
                sb += imageApprox[i][j][0]
                sg += imageApprox[i][j][1]
                sr += imageApprox[i][j][2]
        return math.floor((sr+sg+sb)/(3*(imageApprox.shape[0]*imageApprox.shape[1])))

    def increase_brightness(img, value):
        """increase the brightness relatively to the luminosity return by the approximate_lum function"""
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        lim = 255 - value
        v[v > lim] = 255
        v[v <= lim] += value
        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img

    def get_dominant_color(image, coords):
        """get dominant color in a small rectangle of pixels"""
        coordinateDico = {(0,0): (1,1), (1,0): (3,1), (2,0): (5, 1), (0,1): (1,3), (1,1): (3,3), (2,1): (5,3), (0,2): (1,5), (1,2): (3,5), (2,2): (5,5)}
        sumB, sumG, sumR, b, dlx, dly, (x, y) = 0, 0, 0, 0, math.floor((2/100)*image.shape[0]), math.floor((2/100)*image.shape[1]), coordinateDico[coords]
        for i in range(math.floor(x*(image.shape[0] / 6) - dlx), math.floor(x*(image.shape[0] / 6) + dlx + 1)):
            for j in range(math.floor(y*(image.shape[1] / 6) - dly), math.floor(y*(image.shape[1] / 6) + dly + 1)):
                sumB += image[i][j][0]
                sumG += image[i][j][1]
                sumR += image[i][j][2]
                b += 1
        return [math.floor(sumB/b), math.floor(sumG/b), math.floor(sumR/b)][::-1]

    pic = Camera()
    pic.take_photo()
    image = imutils.rotate_bound(cv2.resize(cv2.imread(pic.path), None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA), 49)[234:362, 306:434]
    image = cv2.GaussianBlur(image, (3, 3), 0)
    #image = increase_brightness(image, value=math.floor(100*math.exp((-approximate_lum(image)**2)/(2*60**2))))

    result = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
    colors = {"MidnightBlue": "bleu", "ForestGreen": "vert", "OrangeRed": "orange", "Orange": "jaune", "DarkRed": "rouge", "DarkGray": "blanc"}
    for i in result:
        i.append(colors[ColorNames.findNearestWebColorName(get_dominant_color(image, tuple(i)))])

    returned = [i[2] for i in result if i[:2] != [1,1]]
    #print(returned)
    #cv2.imshow("test", image)
    #cv2.waitKey(0)
    photo = ImageTk.PhotoImage(Image.fromarray(cv2.resize(image[...,::-1], None, fx=0.4, fy=0.4, interpolation=cv2.INTER_AREA)))
    settings.photos.append(photo)
    t = settings.pos[settings.photos.__len__()]
    label = tk.Label(settings.my_gui.frame2, image=settings.photos[-1])
    settings.images.append(label)
    label.grid(row=t[0], column=t[1], pady=(5, 5))
    v = tk.StringVar()
    v.set(str(returned))
    settings.vs.append(v)
    text = tk.Entry(settings.my_gui.frame2, textvariable=settings.vs[-1], width=55, justify=CENTER)
    settings.texts.append(text)
    text.grid(row=t[2], column=t[3], pady=(5, 5))
    settings.my_gui.frame2.update()
    
    settings.incr += 1
    return returned # ne renvoit pas le cube central
