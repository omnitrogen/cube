import numpy as np
import cv2
import math

''' Memo (do not forget):
    - image[y, x]
    - BGR instead of RGB -> [::-1]
'''

image = cv2.imread("/Users/felixdefrance/.envs/cv/cube/test5.png")
image = cv2.GaussianBlur(image, (3, 3), 0)

# approximation of luminosity in the pic
def approximate_lum(imageApprox):
    sb, sg, sr = 0, 0, 0
    for i in range(imageApprox.shape[0]):
        for j in range(imageApprox.shape[1]):
            sb += imageApprox[i][j][0]
            sg += imageApprox[i][j][1]
            sr += imageApprox[i][j][2]
    return math.floor((sr+sg+sb)/(3*(imageApprox.shape[0]*imageApprox.shape[1])))

# increase the brightness relatively to the luminosity return by the approximate_lum function
def increase_brightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

image = increase_brightness(image, value=math.floor(100*math.exp((-approximate_lum(image)**2)/(2*60**2))))

print("size:", (image.shape[0],image.shape[1]))

# cv2.rectangle(image, (math.floor(1*(image.shape[0] / 6)) - 5, math.floor(1*(image.shape[1] / 6) - 5)), (math.floor(1*(image.shape[0] / 6)) + 5, math.floor(1*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)
# cv2.rectangle(image, (math.floor(3*(image.shape[0] / 6)) - 5, math.floor(1*(image.shape[1] / 6) - 5)), (math.floor(3*(image.shape[0] / 6)) + 5, math.floor(1*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)
# cv2.rectangle(image, (math.floor(5*(image.shape[0] / 6)) - 5, math.floor(1*(image.shape[1] / 6) - 5)), (math.floor(5*(image.shape[0] / 6)) + 5, math.floor(1*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)
# cv2.rectangle(image, (math.floor(1*(image.shape[0] / 6)) - 5, math.floor(3*(image.shape[1] / 6) - 5)), (math.floor(1*(image.shape[0] / 6)) + 5, math.floor(3*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)
# cv2.rectangle(image, (math.floor(3*(image.shape[0] / 6)) - 5, math.floor(3*(image.shape[1] / 6) - 5)), (math.floor(3*(image.shape[0] / 6)) + 5, math.floor(3*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)
# cv2.rectangle(image, (math.floor(5*(image.shape[0] / 6)) - 5, math.floor(3*(image.shape[1] / 6) - 5)), (math.floor(5*(image.shape[0] / 6)) + 5, math.floor(3*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)
# cv2.rectangle(image, (math.floor(1*(image.shape[0] / 6)) - 5, math.floor(5*(image.shape[1] / 6) - 5)), (math.floor(1*(image.shape[0] / 6)) + 5, math.floor(5*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)
# cv2.rectangle(image, (math.floor(3*(image.shape[0] / 6)) - 5, math.floor(5*(image.shape[1] / 6) - 5)), (math.floor(3*(image.shape[0] / 6)) + 5, math.floor(5*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)
# cv2.rectangle(image, (math.floor(5*(image.shape[0] / 6)) - 5, math.floor(5*(image.shape[1] / 6) - 5)), (math.floor(5*(image.shape[0] / 6)) + 5, math.floor(5*(image.shape[1] / 6) + 5)), (0, 0, 255), 1)


def get_dominant_color(image, coords):
    coordinateDico = {(0,0): (1,1), (1,0): (3,1), (2,0): (5, 1), (0,1): (1,3), (1,1): (3,3), (2,1): (5,3), (0,2): (1,5), (1,2): (3,5), (2,2): (5,5)}
    sumB, sumG, sumR, b, dlx, dly, (x, y) = 0, 0, 0, 0, math.floor((2/100)*image.shape[0]), math.floor((2/100)*image.shape[1]), coordinateDico[coords]
    for i in range(math.floor(x*(image.shape[0] / 6) - dlx), math.floor(x*(image.shape[0] / 6) + dlx + 1)):
        for j in range(math.floor(y*(image.shape[1] / 6) - dly), math.floor(y*(image.shape[1] / 6) + dly + 1)):
            sumB += image[i][j][0]
            sumG += image[i][j][1]
            sumR += image[i][j][2]
            b += 1
    return [math.floor(sumB/b), math.floor(sumG/b), math.floor(sumR/b)][::-1]

dom1 = get_dominant_color(image, (0,0))
dom2 = get_dominant_color(image, (0,1))
dom3 = get_dominant_color(image, (0,2))
dom4 = get_dominant_color(image, (1,0))
dom5 = get_dominant_color(image, (1,1))
dom6 = get_dominant_color(image, (1,2))
dom7 = get_dominant_color(image, (2,0))
dom8 = get_dominant_color(image, (2,1))
dom9 = get_dominant_color(image, (2,2))

#cv2.imshow("modify", image)
#cv2.waitKey(0)
# cv2.imshow("img", image)
# cv2.waitKey(0)
#MTX = np.array([[1.64127926e+03, 0.00000000e+00, 1.50380436e+03], [0.00000000e+00, 1.66536863e+03, 1.29941304e+03], [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
#DIST = np.array([[-0.32245647, 0.19393362, -0.00692064, 0.01852231, -0.11396549]])

#modified = cv2.undistort(image, MTX, DIST, None, None)

#modified = cv2.resize(modified, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)


# cv2.imwrite("test.png", modified)


class ColorNames:
    # Src: http://www.w3schools.com/html/html_colornames.asp
    WebColorMap = {}
    # WebColorMap["AliceBlue"] = "#F0F8FF"
    # WebColorMap["AntiqueWhite"] = "#FAEBD7"
    # WebColorMap["Aqua"] = "#00FFFF"
    # WebColorMap["Aquamarine"] = "#7FFFD4"
    # WebColorMap["Azure"] = "#F0FFFF"
    # WebColorMap["Beige"] = "#F5F5DC"
    # WebColorMap["Bisque"] = "#FFE4C4"
    # WebColorMap["Black"] = "#000000"
    # WebColorMap["BlanchedAlmond"] = "#FFEBCD"
    # WebColorMap["Blue"] = "#0000FF"
    # WebColorMap["BlueViolet"] = "#8A2BE2"
    # WebColorMap["Brown"] = "#A52A2A"
    # WebColorMap["BurlyWood"] = "#DEB887"
    # WebColorMap["CadetBlue"] = "#5F9EA0"
    # WebColorMap["Chartreuse"] = "#7FFF00"
    # WebColorMap["Chocolate"] = "#D2691E"
    # WebColorMap["Coral"] = "#FF7F50"
    # WebColorMap["CornflowerBlue"] = "#6495ED"
    # WebColorMap["Cornsilk"] = "#FFF8DC"
    # WebColorMap["Crimson"] = "#DC143C"
    # WebColorMap["Cyan"] = "#00FFFF"
    # WebColorMap["DarkBlue"] = "#00008B"
    # WebColorMap["DarkCyan"] = "#008B8B"
    # WebColorMap["DarkGoldenRod"] = "#B8860B"
    WebColorMap["DarkGray"] = "#A9A9A9"
    # WebColorMap["DarkGrey"] = "#A9A9A9"
    # WebColorMap["DarkGreen"] = "#006400"
    # WebColorMap["DarkKhaki"] = "#BDB76B"
    # WebColorMap["DarkMagenta"] = "#8B008B"
    # WebColorMap["DarkOliveGreen"] = "#556B2F"
    # WebColorMap["Darkorange"] = "#FF8C00"
    # WebColorMap["DarkOrchid"] = "#9932CC"
    WebColorMap["DarkRed"] = "#8B0000"
    # WebColorMap["DarkSalmon"] = "#E9967A"
    # WebColorMap["DarkSeaGreen"] = "#8FBC8F"
    # WebColorMap["DarkSlateBlue"] = "#483D8B"
    # WebColorMap["DarkSlateGray"] = "#2F4F4F"
    # WebColorMap["DarkSlateGrey"] = "#2F4F4F"
    # WebColorMap["DarkTurquoise"] = "#00CED1"
    # WebColorMap["DarkViolet"] = "#9400D3"
    # WebColorMap["DeepPink"] = "#FF1493"
    # WebColorMap["DeepSkyBlue"] = "#00BFFF"
    # WebColorMap["DimGray"] = "#696969"
    # WebColorMap["DimGrey"] = "#696969"
    # WebColorMap["DodgerBlue"] = "#1E90FF"
    # WebColorMap["FireBrick"] = "#B22222"
    # WebColorMap["FloralWhite"] = "#FFFAF0"
    WebColorMap["ForestGreen"] = "#228B22"
    # WebColorMap["Fuchsia"] = "#FF00FF"
    # WebColorMap["Gainsboro"] = "#DCDCDC"
    # WebColorMap["GhostWhite"] = "#F8F8FF"
    # WebColorMap["Gold"] = "#FFD700"
    # WebColorMap["GoldenRod"] = "#DAA520"
    # WebColorMap["Gray"] = "#808080"
    # WebColorMap["Grey"] = "#808080"
    # WebColorMap["Green"] = "#008000"
    # WebColorMap["GreenYellow"] = "#ADFF2F"
    # WebColorMap["HoneyDew"] = "#F0FFF0"
    # WebColorMap["HotPink"] = "#FF69B4"
    # WebColorMap["IndianRed"] = "#CD5C5C"
    # WebColorMap["Indigo"] = "#4B0082"
    # WebColorMap["Ivory"] = "#FFFFF0"
    # WebColorMap["Khaki"] = "#F0E68C"
    # WebColorMap["Lavender"] = "#E6E6FA"
    # WebColorMap["LavenderBlush"] = "#FFF0F5"
    # WebColorMap["LawnGreen"] = "#7CFC00"
    # WebColorMap["LemonChiffon"] = "#FFFACD"
    # WebColorMap["LightBlue"] = "#ADD8E6"
    # WebColorMap["LightCoral"] = "#F08080"
    # WebColorMap["LightCyan"] = "#E0FFFF"
    # WebColorMap["LightGoldenRodYellow"] = "#FAFAD2"
    # WebColorMap["LightGray"] = "#D3D3D3"
    # WebColorMap["LightGrey"] = "#D3D3D3"
    # WebColorMap["LightGreen"] = "#90EE90"
    # WebColorMap["LightPink"] = "#FFB6C1"
    # WebColorMap["LightSalmon"] = "#FFA07A"
    # WebColorMap["LightSeaGreen"] = "#20B2AA"
    # WebColorMap["LightSkyBlue"] = "#87CEFA"
    # WebColorMap["LightSlateGray"] = "#778899"
    # WebColorMap["LightSlateGrey"] = "#778899"
    # WebColorMap["LightSteelBlue"] = "#B0C4DE"
    # WebColorMap["LightYellow"] = "#FFFFE0"
    # WebColorMap["Lime"] = "#00FF00"
    # WebColorMap["LimeGreen"] = "#32CD32"
    # WebColorMap["Linen"] = "#FAF0E6"
    # WebColorMap["Magenta"] = "#FF00FF"
    # WebColorMap["Maroon"] = "#800000"
    # WebColorMap["MediumAquaMarine"] = "#66CDAA"
    # WebColorMap["MediumBlue"] = "#0000CD"
    # WebColorMap["MediumOrchid"] = "#BA55D3"
    # WebColorMap["MediumPurple"] = "#9370D8"
    # WebColorMap["MediumSeaGreen"] = "#3CB371"
    # WebColorMap["MediumSlateBlue"] = "#7B68EE"
    # WebColorMap["MediumSpringGreen"] = "#00FA9A"
    # WebColorMap["MediumTurquoise"] = "#48D1CC"
    # WebColorMap["MediumVioletRed"] = "#C71585"
    WebColorMap["MidnightBlue"] = "#191970"
    # WebColorMap["MintCream"] = "#F5FFFA"
    # WebColorMap["MistyRose"] = "#FFE4E1"
    # WebColorMap["Moccasin"] = "#FFE4B5"
    # WebColorMap["NavajoWhite"] = "#FFDEAD"
    # WebColorMap["Navy"] = "#000080"
    # WebColorMap["OldLace"] = "#FDF5E6"
    # WebColorMap["Olive"] = "#808000"
    # WebColorMap["OliveDrab"] = "#6B8E23"
    WebColorMap["Orange"] = "#FFA500"
    WebColorMap["OrangeRed"] = "#FF4500"
    # WebColorMap["Orchid"] = "#DA70D6"
    # WebColorMap["PaleGoldenRod"] = "#EEE8AA"
    # WebColorMap["PaleGreen"] = "#98FB98"
    # WebColorMap["PaleTurquoise"] = "#AFEEEE"
    # WebColorMap["PaleVioletRed"] = "#D87093"
    # WebColorMap["PapayaWhip"] = "#FFEFD5"
    # WebColorMap["PeachPuff"] = "#FFDAB9"
    # WebColorMap["Peru"] = "#CD853F"
    # WebColorMap["Pink"] = "#FFC0CB"
    # WebColorMap["Plum"] = "#DDA0DD"
    # WebColorMap["PowderBlue"] = "#B0E0E6"
    # WebColorMap["Purple"] = "#800080"
    # WebColorMap["Red"] = "#FF0000"
    # WebColorMap["RosyBrown"] = "#BC8F8F"
    # WebColorMap["RoyalBlue"] = "#4169E1"
    # WebColorMap["SaddleBrown"] = "#8B4513"
    # WebColorMap["Salmon"] = "#FA8072"
    # WebColorMap["SandyBrown"] = "#F4A460"
    # WebColorMap["SeaGreen"] = "#2E8B57"
    # WebColorMap["SeaShell"] = "#FFF5EE"
    # WebColorMap["Sienna"] = "#A0522D"
    # WebColorMap["Silver"] = "#C0C0C0"
    # WebColorMap["SkyBlue"] = "#87CEEB"
    # WebColorMap["SlateBlue"] = "#6A5ACD"
    # WebColorMap["SlateGray"] = "#708090"
    # WebColorMap["SlateGrey"] = "#708090"
    # WebColorMap["Snow"] = "#FFFAFA"
    # WebColorMap["SpringGreen"] = "#00FF7F"
    # WebColorMap["SteelBlue"] = "#4682B4"
    # WebColorMap["Tan"] = "#D2B48C"
    # WebColorMap["Teal"] = "#008080"
    # WebColorMap["Thistle"] = "#D8BFD8"
    # WebColorMap["Tomato"] = "#FF6347"
    # WebColorMap["Turquoise"] = "#40E0D0"
    # WebColorMap["Violet"] = "#EE82EE"
    # WebColorMap["Wheat"] = "#F5DEB3"
    # WebColorMap["White"] = "#FFFFFF"
    # WebColorMap["WhiteSmoke"] = "#F5F5F5"
    # WebColorMap["Yellow"] = "#FFFF00"
    # WebColorMap["YellowGreen"] = "#9ACD32"

    def findNearestColorName(a, Map):
        mindiff = None
        for d in Map:
            r, g, b = ColorNames.rgbFromStr(Map[d])
            diff = abs(a[0] - r) * 256 + abs(a[1] - g) * 256 + abs(a[2] - b) * 256
            if mindiff is None or diff < mindiff:
                mindiff = diff
                mincolorname = d
        return mincolorname

    def rgbFromStr(s):
        # s starts with a #.
        (r, g, b) = (int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16))
        return r, g, b

    def findNearestWebColorName(a):
        return ColorNames.findNearestColorName(a, ColorNames.WebColorMap)

    def findNearestImageMagickColorName(a):
        return ColorNames.findNearestColorName(a, ColorNames.ImageMagickColorMap)

colors = {"MidnightBlue": "blue", "ForestGreen": "green", "OrangeRed": "orange", "Orange": "yellow", "DarkRed": "red", "DarkGray": "white"}

print(colors[ColorNames.findNearestWebColorName(dom1)])
print(colors[ColorNames.findNearestWebColorName(dom2)])
print(colors[ColorNames.findNearestWebColorName(dom3)])
print(colors[ColorNames.findNearestWebColorName(dom4)])
print(colors[ColorNames.findNearestWebColorName(dom5)])
print(colors[ColorNames.findNearestWebColorName(dom6)])
print(colors[ColorNames.findNearestWebColorName(dom7)])
print(colors[ColorNames.findNearestWebColorName(dom8)])
print(colors[ColorNames.findNearestWebColorName(dom9)])
