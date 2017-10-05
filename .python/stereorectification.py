import numpy as np
import dill

##savefile = 'ir_matrices2.pkl'
##savefile = 'rgb_matrices.pkl'
##savefile = 'example_matrices.pkl'
##savefile = '_matrices_12_ESS.pkl'
##savefile = 'rgb_matrices_13_print.pkl'
savefile = 'ir_matrices_13_print.pkl'
dill.load_session(savefile)


##import _ir_matrices as cal
##import _rgb_matrices as cal

##print 'cal.total_error:\t' + str(cal.total_error)
##print 'cal.ret:\t\t' + str(cal.ret)
##print 'cal.mtx.shape:\t\t' + str(cal.mtx.shape)
##print 'cal.dist.shape:\t\t' + str(cal.dist.shape)
##print 'cal.rvecs.shape:\t' + str(cal.rvecs.shape)
##print 'cal.tvecs.shape:\t' + str(cal.tvecs.shape)
##print 'cal.objpoints.shape:\t' + str(cal.objpoints.shape)
##print 'np.shape(cal.imgpoints):' + str(np.shape(cal.imgpoints))
##print 'cal.resolution:\t\t' + str(cal.resolution)
##print 'cal.imgpoints2.shape:\t' + str(cal.imgpoints2.shape)

print 'total_error:\t\t' + str(total_error)
print 'ret:\t\t\t' + str(ret)
print 'mtx.shape:\t\t' + str(mtx.shape)
print 'dist.shape:\t\t' + str(dist.shape)
print 'rvecs.shape:\t\t' + str(np.shape(rvecs))
print 'tvecs.shape:\t\t' + str(np.shape(tvecs))
print 'objpoints.shape:\t' + str(np.shape(objpoints))
print 'np.shape(imgpoints):\t' + str(np.shape(imgpoints))
print 'resolution:\t\t' + str(gray.shape[::-1])
print 'imgpoints2.shape:\t' + str(np.shape(imgpoints2))

##img_path = 'C:/Users/d7rob/thesis/chess/master_set/rgb_7x6/'
##fname = 'img_2017-09-30_17-37-27.000_rgb_1_has_7x6_corners.jpg'
##img_path = 'C:/Users/d7rob/thesis/front_garden_4/'
##fname = 'img_2017-09-30_17-43-34.000_ir_1.jpg'
##img_path = 'C:/Users/d7rob/thesis/home_lab_window/ndvi/'
##fname = 'img_2017-09-29_16-38-45.006_ir_1.jpg'
img_path = 'C:/Users/d7rob/thesis/longridge/'
##fname = '20170923_174647.jpg'
##img_path = 'L:/Backups/thesis/longridge/rgb'
##img_path = 'L:/Backups/thesis/longridge/ir'
##fname = 'img1_2017-09-27_12-43-50.000_156.jpg'
fname = 'ir_2017-09-27_12-45-38.000_1.jpg'
img = cv2.imread(img_path + fname)
##img = cv2.imread('chess/left12.jpg')
h, w = img.shape[:2]
##print h, w
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
print newcameramtx, roi

### undistort
##mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w,h), 5)
##print mapx.shape, mapy.shape
##dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
### crop the image
####x, y, w, h = roi
####dst = dst[y:y+h, x:x+w]
####img = cv2.imwrite('chess/left12_undistorted.jpg', dst)

# undistort
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
# crop the image
##x, y, w, h = roi
##dst = dst[y:y+h, x:x+w]
####cv2.imwrite('calibresult.png', dst)
k_crop = 1
##dst2 = cv2.getRectSubPix(dst, ((int)(k_crop*h), (int)(k_crop*w)), (0, 0))
##dst2 = cv2.getRectSubPix(dst, (w, h), (1, 1))
dst2 = dst[(int)(h*(1-k_crop)):(int)(h*k_crop), (int)(w*(1-k_crop)):(int)(w*k_crop)]
print dst2.shape

undistorted_path = img_path + fname[:-4] + '_undistorted.jpg'
print undistorted_path
cv2.imwrite(undistorted_path, dst2)
