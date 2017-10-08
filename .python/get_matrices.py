import cv2 #, numpy, matplotlib
import numpy as np
from matplotlib import pyplot as plt
import glob
import dill
from tqdm import tqdm
import os

img_type = 'ir'
##img_type = 'rgb'
##img_type = 'example'

_x = 15
_y = 15

savefile = img_type + '_matrices_13_print.pkl'
##root_path = 'C:/Users/d7rob/thesis/chess/master_set/'
root_path = 'C:/Users/d7rob/thesis/chess/13_print/ir_ready/'
##root_path = 'chess/'
##images = glob.glob('chess/*.jpg')
##images = glob.glob('L:/Backups/thesis/chess/rgb/compressed/picked/*.jpg')
##images = glob.glob('C:/Users/d7rob/thesis/chess/master_set/rgb_7x6/*.jpg')
##images = glob.glob(root_path + img_type + '_7x6/*.jpg')
##images = glob.glob(root_path + img_type + '_15x15/*.jpg')
images = glob.glob(root_path + '/*.jpg')

##gray = 0
# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((_y*_x,3), np.float32)
objp[:,:2] = np.mgrid[0:_x,0:_y].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

for fname in tqdm(images):
    print fname
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Find the chess board corners
    
    flags = cv2.CALIB_CB_ADAPTIVE_THRESH + \
            cv2.CALIB_CB_NORMALIZE_IMAGE + \
            cv2.CALIB_CB_FILTER_QUADS + \
            cv2.CALIB_CB_FAST_CHECK
    ret, corners = cv2.findChessboardCorners(gray, (_x,_y), flags)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2=cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        cv2.drawChessboardCorners(img, (_x,_y), corners2, ret)
        draw_path = root_path + img_type + '_'+str(_x)+'x'+str(_y)+'_drawn/' + os.path.basename(fname)[:-4] + '_drawn.jpg'
        print draw_path
        cv2.imwrite(draw_path, img)
##        cv2.imshow('img', img)
##        cv2.waitKey(500)
cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
print ret, mtx, dist, rvecs, tvecs
##img = cv2.imread('C:/Users/d7rob/thesis/chess/rgb/img1_2017-09-25_23-18-52.001_1.jpg')
####img = cv2.imread('chess/left12.jpg')
##h,  w = img.shape[:2]
##newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

mean_error = 0
for i in tqdm(xrange(len(objpoints))):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2)/len(imgpoints2)
    mean_error += error
total_error = mean_error/len(objpoints)
print( "total error: {}".format(total_error) )

dill.dump_session(savefile)

### undistort
##mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w,h), 5)
##dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
### crop the image
##x, y, w, h = roi
##dst = dst[y:y+h, x:x+w]
##cv2.imwrite('calibresult.png', dst)

### undistort
##dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
### crop the image
##x, y, w, h = roi
##dst = dst[y:y+h, x:x+w]
##cv2.imwrite('calibresult.png', dst)

##print "ret: " + str(ret)
##print "mtx: " + str(mtx)
##print "dist: " + str(dist)
##print "rvecs: " + str(rvecs)
##print "tvecs: " + str(tvecs)


### Load an color image in grayscale
##img = cv2.imread('messi5.jpg',0)
##
##cv2.imshow('image',img)
##
##plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
##plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
##plt.show()
##
##k = cv2.waitKey(0) & 0xFF
##if k == 27:         # wait for ESC key to exit
##    cv2.destroyAllWindows()
##elif k == ord('s'): # wait for 's' key to save and exit
##    cv2.imwrite('messigray.png',img)
##    cv2.destroyAllWindows()

### Create a black image
##img = np.zeros((512,512,3), np.uint8)
### Draw a diagonal blue line with thickness of 5 px
##cv2.line(img,(0,0),(511,511),(255,0,0),5)
##cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
##cv2.circle(img,(447,63), 63, (0,0,255), -1)
##cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
####
##pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
##pts = pts.reshape((-1,1,2))
##cv2.polylines(img,[pts],True,(0,255,255))
####
##font = cv2.FONT_HERSHEY_SIMPLEX
##cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
##
####cv2.imshow('image',img)
##plt.imshow(img)
##plt.show()

##events = [i for i in dir(cv2) if 'EVENT' in i]
##print( events )
##
### mouse callback function
##def draw_circle(event,x,y,flags,param):
##    if event == cv2.EVENT_LBUTTONDBLCLK:
##        cv2.circle(img,(x,y),100,(255,0,0),-1)
### Create a black image, a window and bind the function to window
##img = np.zeros((512,512,3), np.uint8)
##cv2.namedWindow('image')
##cv2.setMouseCallback('image',draw_circle)
##while(1):
##    cv2.imshow('image',img)
##    if cv2.waitKey(20) & 0xFF == 27:
##        break
##cv2.destroyAllWindows()
