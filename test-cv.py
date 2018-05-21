import os
import math
import cv2
import numpy as np
import imutils

from goprocam import GoProCamera
from goprocam import constants

from nearest_color import ColorNames


class ColorFinder(object):
    '''ColorFinder: take an image path, transform the image and return color of each face'''
    def __init__(self, path):
        self.image = cv2.imread(path)

    def modify(self):
        """ delete the distortion (gopro cam have natural distortion) and then resize the pic """
        MTX = np.array([[1.64127926e+03, 0.00000000e+00, 1.50380436e+03], [0.00000000e+00, 1.66536863e+03, 1.29941304e+03], [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
        DIST = np.array([[-0.32245647, 0.19393362, -0.00692064, 0.01852231, -0.11396549]])
        self.image = cv2.undistort(self.image, MTX, DIST, None, None)
        self.image = cv2.resize(self.modified, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
        #cv2.imshow("modify", self.image)
        #cv2.waitKey(0)

    def analyse(self):
        """ analyse the cube and return 9 colors (one for each cube on a face) """

        print("size:", self.image.shape[0], self.image.shape[1])

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

        self.image = cv2.GaussianBlur(self.image, (3, 3), 0)
        self.image = increase_brightness(self.image, value=math.floor(100*math.exp((-approximate_lum(self.image)**2)/(2*60**2))))

        # cv2.rectangle(image, (math.floor(1*(image.shape[0] / 6)) - 5, math.floor(1*(image.shape[1] / 6) - 5)), (math.floor(1*(image.shape[0] / 6)) + 5, math.floor(1*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)
        # cv2.rectangle(image, (math.floor(3*(image.shape[0] / 6)) - 5, math.floor(1*(image.shape[1] / 6) - 5)), (math.floor(3*(image.shape[0] / 6)) + 5, math.floor(1*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)
        # cv2.rectangle(image, (math.floor(5*(image.shape[0] / 6)) - 5, math.floor(1*(image.shape[1] / 6) - 5)), (math.floor(5*(image.shape[0] / 6)) + 5, math.floor(1*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)
        # cv2.rectangle(image, (math.floor(1*(image.shape[0] / 6)) - 5, math.floor(3*(image.shape[1] / 6) - 5)), (math.floor(1*(image.shape[0] / 6)) + 5, math.floor(3*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)
        # cv2.rectangle(image, (math.floor(3*(image.shape[0] / 6)) - 5, math.floor(3*(image.shape[1] / 6) - 5)), (math.floor(3*(image.shape[0] / 6)) + 5, math.floor(3*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)
        # cv2.rectangle(image, (math.floor(5*(image.shape[0] / 6)) - 5, math.floor(3*(image.shape[1] / 6) - 5)), (math.floor(5*(image.shape[0] / 6)) + 5, math.floor(3*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)
        # cv2.rectangle(image, (math.floor(1*(image.shape[0] / 6)) - 5, math.floor(5*(image.shape[1] / 6) - 5)), (math.floor(1*(image.shape[0] / 6)) + 5, math.floor(5*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)
        # cv2.rectangle(image, (math.floor(3*(image.shape[0] / 6)) - 5, math.floor(5*(image.shape[1] / 6) - 5)), (math.floor(3*(image.shape[0] / 6)) + 5, math.floor(5*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)
        # cv2.rectangle(image, (math.floor(5*(image.shape[0] / 6)) - 5, math.floor(5*(image.shape[1] / 6) - 5)), (math.floor(5*(image.shape[0] / 6)) + 5, math.floor(5*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)

        result = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
        colors = {"MidnightBlue": "blue", "ForestGreen": "green", "OrangeRed": "orange", "Orange": "yellow", "DarkRed": "red", "DarkGray": "white"}
        for i in result:
            i.append(colors[ColorNames.findNearestWebColorName(get_dominant_color(self.image, tuple(i)))])

        return [i[2] for i in result if i[:2] != [1,1]] # ne renvoit pas le cube central



class Camera(GoProCamera.GoPro):
    """ GoPro class """

    def __init__(self):
        """ Class initialiser """
        GoProCamera.GoPro.__init__(self, constants.gpcontrol)
        self.path = str()

    def take_photo(self):
        """ take pic, download it and return the path of the pic """
        GoProCamera.GoPro.take_photo(self)
        GoProCamera.GoPro.downloadLastMedia(self)
        self.path = os.getcwd() + "/" + "118GOPRO-" + str(self.getMediaInfo("file"))

test = Camera()
test.take_photo()
image = cv2.imread(test.path)
resized = cv2.resize(image, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
#cv2.imshow("image", resized)
#cv2.waitKey(0)

rotated = imutils.rotate_bound(resized, -5)
#cv2.imshow("rotated", rotated)
#cv2.waitKey(0)

print(rotated.shape[:2])
rotated2 = rotated[193:287, 214:309]
#cv2.imshow("rotated", rotated2)
#cv2.waitKey(0)
#cv2.imwrite("/Users/felixdefrance/Downloads/sisisi.png", rotated2)

finder = ColorFinder("/Users/felixdefrance/Downloads/sisisi.png")
#finder.modify()
print(finder.analyse())
