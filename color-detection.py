import numpy as np
import cv2
from sklearn.cluster import MiniBatchKMeans

img = cv2.imread('path/to/image')

img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
gray = cv2.GaussianBlur(img, (3, 3), 0)
gray = cv2.cvtColor(gray,cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray,9,75,75)

# il va falloir appliquer un treshold ici car il va y avoir les tiges reliées au moteur qui viendront perturber la fonction "goodFeaturesToTrack"...

corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)

abscisses = [elt[0][0] for elt in corners.tolist()]
ordonnees = [elt[0][1] for elt in corners.tolist()]

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow("img", img)
cv2.waitKey(0)

print(min(ordonnees), max(ordonnees), min(abscisses), max(abscisses))
crop = img[min(ordonnees):max(ordonnees),min(abscisses):max(abscisses)].copy()

#cv2.imwrite("crop.png", crop)
cv2.imshow("crop",crop)
cv2.waitKey(0)


# grab width and height of the cropped image
(h, w) = crop.shape[:2]
print(h, w)

# convert the image from the RGB color space to the L*a*b*
# color space -- since we will be clustering using k-means
# which is based on the euclidean distance, we'll use the
# L*a*b* color space where the euclidean distance implies
# perceptual meaning
crop = cv2.cvtColor(crop, cv2.COLOR_BGR2LAB)

# reshape the image into a feature vector so that k-means
# can be applied
crop = crop.reshape((crop.shape[0] * crop.shape[1], 3))

# apply k-means using the specified number of clusters and
# then create the quantized image based on the predictions
clt = MiniBatchKMeans(n_clusters = 10)
labels = clt.fit_predict(crop)
quant = clt.cluster_centers_.astype("uint8")[labels]

# reshape the feature vectors to images
quant = quant.reshape((h, w, 3))
crop = crop.reshape((h, w, 3))

# convert from L*a*b* to RGB
quant = cv2.cvtColor(quant, cv2.COLOR_LAB2BGR)
crop = cv2.cvtColor(crop, cv2.COLOR_LAB2BGR)

# display the images and wait for a keypress
cv2.imshow("color quantization", np.hstack([quant]))
cv2.waitKey(0)

# une image est une matrice numpy, donc si on veut reflechir avec un repere orthonorme, l'origine sera en haut a gauche 

# renvoit la couleur au format BGR du pixel situe en (a,b)
a = int(input("a:"))
b = int(input("b:"))
print(quant[a,b])
