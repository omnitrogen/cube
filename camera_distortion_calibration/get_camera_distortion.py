import numpy as np
import cv2


#from: http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html


# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

img = cv2.imread('pic2.JPG') 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Find the chess board corners
ret, corners = cv2.findChessboardCorners(gray, (7,6),None)

# If found, add object points, image points (after refining them)
if ret == True:
    objpoints.append(objp)

    corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
    imgpoints.append(corners2)

    # Draw and display the corners
    img = cv2.drawChessboardCorners(img, (7,6), corners2,ret)
    rsz = cv2.resize(img,None,fx=0.2, fy=0.2, interpolation = cv2.INTER_AREA)
    cv2.imshow('rsz',rsz)
    cv2.waitKey(0)

cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
print(ret, type(ret), mtx, type(mtx), dist, type(dist))

'''
Return:

ret = 1.6848447161437363

mtx = [[  1.64127926e+03   0.00000000e+00   1.50380436e+03]
 [  0.00000000e+00   1.66536863e+03   1.29941304e+03]
 [  0.00000000e+00   0.00000000e+00   1.00000000e+00]]

dist = [[-0.32245647  0.19393362 -0.00692064  0.01852231 -0.11396549]]

rvecs = [array([[-0.18822089],
       [ 0.07518308],
       [-1.5168964 ]])]

tvecs = [array([[-1.95332275],
       [ 2.85257176],
       [ 6.10126539]])]

We use these parameters in the main program.
'''
