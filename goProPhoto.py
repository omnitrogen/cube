from goprocam import GoProCamera
from goprocam import constants
import time
# https://github.com/KonradIT/gopro-py-api

gpCam = GoProCamera.GoPro(constants.gpcontrol)
gpCam.take_photo()
gpCam.downloadLastMedia()

print(gpCam.getMediaInfo("file"))

