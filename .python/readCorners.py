import glob, cv2
import numpy as np
from matplotlib import pyplot as plt

##images = glob.glob('L:/Backups/thesis/chess/rgb/compressed2/picked/*.jpg')
root_dir = 'C:/Users/d7rob/thesis/chess/13_print/compressed'
images = glob.glob(root_dir + '/*.jpg')
print images
img = cv2.imread(images[0])

##gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##gray = img

##plt.imshow(gray)
##plt.show()

cv2.imshow('gray', gray)
cv2.waitKey(500)
cv2.destroyAllWindows()

flags = cv2.CALIB_CB_ADAPTIVE_THRESH + \
        cv2.CALIB_CB_NORMALIZE_IMAGE + \
        cv2.CALIB_CB_FILTER_QUADS + \
        cv2.CALIB_CB_FAST_CHECK
##flags = None

x = 15
y = 15
ret, corners = cv2.findChessboardCorners(gray, (x,y), flags)

print corners, ret

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((x*y,3), np.float32)
objp[:,:2] = np.mgrid[0:x,0:y].T.reshape(-1,2)
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
if ret == True or True:
    objpoints.append(objp)
    corners2=cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
    imgpoints.append(corners)
    # Draw and display the corners
    cv2.drawChessboardCorners(img, (x,y), corners2, ret)
    cv2.imshow('img', img)
    cv2.imwrite((str(images[0][:-4]) + '_corners.jpg'), img)
    cv2.waitKey(1000)
cv2.destroyAllWindows()
