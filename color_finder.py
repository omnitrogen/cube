import numpy as np
import cv2
from sklearn.cluster import MiniBatchKMeans
from nearest_color import ColorNames
from camera import Camera


class ColorFinder:
	""" ColorFinder class """

	def __init__(self, path):
		""" Class initialiser """
		self.image = cv2.imread(path)

	def modify(self):
		""" delete the distortion (gopro cam have natural distortion) and then resize the pic """
		MTX = np.array([[1.64127926e+03, 0.00000000e+00, 1.50380436e+03], [0.00000000e+00, 1.66536863e+03, 1.29941304e+03], [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
		DIST = np.array([[-0.32245647, 0.19393362, -0.00692064, 0.01852231, -0.11396549]])

		self.modify = cv2.undistort(self.image, MTX, DIST, None, None)
		self.modify = cv2.resize(self.modify,None,fx=0.2, fy=0.2, interpolation = cv2.INTER_AREA)
		cv2.imshow("modify", self.modify)
		cv2.waitKey(0)

	def analyse(self):
		""" analyse the cube and return 9 colors (one for each cube on a face) """
		img = cv2.fastNlMeansDenoisingColored(self.modify,None,10,10,7,21)
		gray = cv2.GaussianBlur(img, (3, 3), 0)
		gray = cv2.cvtColor(gray,cv2.COLOR_BGR2GRAY)
		gray = cv2.bilateralFilter(gray,9,75,75)

		corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
		corners = np.int0(corners)

		abscisses = [elt[0][0] for elt in corners.tolist()]
		ordonnees = [elt[0][1] for elt in corners.tolist()]

		for i in corners:
			x, y = i.ravel()
			cv2.circle(img, (x, y), 3, 255, -1)

		cv2.imshow("img", img)
		cv2.waitKey(0)

		print(min(ordonnees), max(ordonnees), min(abscisses), max(abscisses))
		crop = img[min(ordonnees):max(ordonnees),min(abscisses):max(abscisses)].copy()

		cv2.imshow("crop", crop)
		cv2.waitKey(0)

		# grab width and height of the cropped image
		(height, width) = crop.shape[:2]
		print("h, w :", height, width)

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
		clt = MiniBatchKMeans(n_clusters=6)
		labels = clt.fit_predict(crop)
		quant = clt.cluster_centers_.astype("uint8")[labels]

		# reshape the feature vectors to images
		quant = quant.reshape((height, width, 3))
		crop = crop.reshape((height, width, 3))

		# convert from L*a*b* to RGB
		quant = cv2.cvtColor(quant, cv2.COLOR_LAB2BGR)
		crop = cv2.cvtColor(crop, cv2.COLOR_LAB2BGR)

		# display the images and wait for a keypress
		cv2.rectangle(quant,(height//12, width//12,),(3*(height//12), 3*(width//12)),(0,255,0),1)
		cv2.rectangle(quant,(5*(height//12), width//12),(7*(height//12), 3*(width//12)),(0,255,0),1)
		cv2.rectangle(quant,(9*(height//12), width//12),(11*(height//12), 3*(width//12)),(0,255,0),1)

		cv2.rectangle(quant,(height//12, 5*(width//12)),(3*(height//12), 7*(width//12)),(0,255,0),1)
		cv2.rectangle(quant,(5*(height//12), 5*(width//12)),(7*(height//12), 7*(width//12)),(0,255,0),1)
		cv2.rectangle(quant,(9*(height//12), 5*(width//12)),(11*(height//12), 7*(width//12)),(0,255,0),1)

		cv2.rectangle(quant,(height//12, 9*(width//12)),(3*(height//12), 11*(width//12)),(0,255,0),1)
		cv2.rectangle(quant,(5*(height//12), 9*(width//12)),(7*(height//12), 11*(width//12)),(0,255,0),1)
		cv2.rectangle(quant,(9*(height//12), 9*(width//12)),(11*(height//12), 11*(width//12)),(0,255,0),1)

		# (y, x) 

		a = ((height//6), (width//6))
		b = ((height//6), (3*(width//6)))
		c = ((height//6), (5*(width//6)))
		d = ((3*(height//6)), (width//6))
		e = ((3*(height//6)), (3*(width//6)))
		f = ((3*(height//6)), (5*(width//6)))
		g = ((5*(height//6)), (width//6))
		h = ((5*(height//6)), (3*(width//6)))
		i = ((5*(height//6)), (5*(width//6)))

		# BGR format (not RGB)
		print("\n")
		colors = {"MidnightBlue": "blue", "ForestGreen": "green", "OrangeRed": "orange", "Orange": "yellow", "DarkRed": "red", "DarkGray": "white"}
		print("a :", colors[ColorNames.findNearestWebColorName(tuple(list(quant[a])[::-1]))])
		print("b :", colors[ColorNames.findNearestWebColorName(tuple(list(quant[b])[::-1]))])
		print("c :", colors[ColorNames.findNearestWebColorName(tuple(list(quant[c])[::-1]))])
		print("d :", colors[ColorNames.findNearestWebColorName(tuple(list(quant[d])[::-1]))])
		print("e :", colors[ColorNames.findNearestWebColorName(tuple(list(quant[e])[::-1]))])
		print("f :", colors[ColorNames.findNearestWebColorName(tuple(list(quant[f])[::-1]))])
		print("g :", colors[ColorNames.findNearestWebColorName(tuple(list(quant[g])[::-1]))])
		print("h :", colors[ColorNames.findNearestWebColorName(tuple(list(quant[h])[::-1]))])
		print("i :", colors[ColorNames.findNearestWebColorName(tuple(list(quant[i])[::-1]))])

		cv2.imshow("color quantization", np.hstack([quant]))
		cv2.waitKey(0)



def main():
	#camera = Camera()
	#camera.take_photo()
	#print(camera.path) # path of the pic taken by the gopro
	finder = ColorFinder("/Users/felixdefrance/Desktop/rubik\'s-pic/naturel.JPG")
	finder.modify()
	finder.analyse()

if __name__ == "__main__":
	main()