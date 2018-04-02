import numpy as np
import cv2
import glob
#STACKERFLOW
#https://stackoverflow.com/questions/31249037/calibrating-webcam-using-python-and-opencv-error?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa


# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

cbrow = 5 #https://stackoverflow.com/questions/31249037/calibrating-webcam-using-python-and-opencv-error?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
cbcol = 5

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((cbrow * cbcol, 3), np.float32)
objp[:, :2] = np.mgrid[0:cbcol, 0:cbrow].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('*.jpg')
print(images)

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray,(cbrow,cbcol),None)
    print(ret)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (cbrow,cbcol), corners2,ret)
        cv2.imshow('img',img)
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
        #print(gray.shape[::-1])
       # print(imgpoints)

img = cv2.imread('test16.png')
h,w = img.shape[:2]
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
cv2.imwrite('cal1.png',dst)
#cv2.imshow('imgafe',dst)

img = cv2.imread('cal1.png')
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
cv2.imwrite('cal2.png',dst)

img = cv2.imread('cal2.png')
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
cv2.imwrite('cal3.png',dst)


## crop the image
#x,y,w,h = roi
#dst = dst[y:y+h, x:x+w]


cv2.waitKey(500)
#cv2.destroyAllWindows()
