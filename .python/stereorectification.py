import numpy as np
import dill

class Matrices:
    def __init__(self, total_error, ret, mtx, dist, rvecs, tvecs, imgpoints, objpoints, gray):
        self.total_error = total_error
        self.ret = ret
        self.mtx = mtx
        self.dist = dist
        self.rvecs = rvecs
        self.tvecs = tvecs
        self.imgpoints = imgpoints
        self.objpoints = objpoints
        self.gray = gray

    def print_values(self):
        print 'total_error:\t\t' + str(self.total_error)
        print 'ret:\t\t\t' + str(self.ret)
        print 'mtx.shape:\t\t' + str(self.mtx.shape)
        print 'dist.shape:\t\t' + str(self.dist.shape)
        print 'rvecs.shape:\t\t' + str(np.shape(self.rvecs))
        print 'tvecs.shape:\t\t' + str(np.shape(self.tvecs))
        print 'objpoints.shape:\t' + str(np.shape(self.objpoints))
        print 'np.shape(imgpoints):\t' + str(np.shape(self.imgpoints))
        print 'resolution:\t\t' + str(self.gray.shape[::-1])
##        print 'imgpoints2.shape:\t' + str(np.shape(imgpoints2))

savefile = 'rgb_matrices.pkl'
dill.load_session(savefile)
rgb_mat = Matrices(total_error, ret, mtx, dist, rvecs, tvecs, imgpoints, objpoints, gray)
rgb_mat.print_values()

savefile = 'ir_matrices.pkl'
dill.load_session(savefile)
ir_mat = Matrices(total_error, ret, mtx, dist, rvecs, tvecs, imgpoints, objpoints, gray)
ir_mat.print_values()

##savefile = 'example_matrices.pkl'
##savefile = '_matrices_12_ESS.pkl'
##savefile = 'rgb_matrices_13_print.pkl'
##savefile = 'ir_matrices_13_print.pkl'
##dill.load_session(savefile)

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

# undistort
mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w,h), cv2.CV_32FC1) # 5
print mapx.shape, mapy.shape
dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
### crop the image
####x, y, w, h = roi
####dst = dst[y:y+h, x:x+w]
####img = cv2.imwrite('chess/left12_undistorted.jpg', dst)

### undistort
##dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
### crop the image
####x, y, w, h = roi
####dst = dst[y:y+h, x:x+w]
######cv2.imwrite('calibresult.png', dst)
k_crop = 1
##dst2 = cv2.getRectSubPix(dst, ((int)(k_crop*h), (int)(k_crop*w)), (0, 0))
##dst2 = cv2.getRectSubPix(dst, (w, h), (1, 1))
dst2 = dst[(int)(h*(1-k_crop)):(int)(h*k_crop), (int)(w*(1-k_crop)):(int)(w*k_crop)]
print dst2.shape

undistorted_path = img_path + fname[:-4] + '_undistorted.jpg'
print undistorted_path
##cv2.imwrite(undistorted_path, dst2)
