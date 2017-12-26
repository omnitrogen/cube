from goprocam import GoProCamera
from goprocam import constants
import os


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




if __name__ == "__main__":
	test = Camera()
	test.take_photo()
	print(test.path)

