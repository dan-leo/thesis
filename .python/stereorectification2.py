import numpy as np
import dill

##print ": " + str()
def pp(val):
    print '::\t' + str(val)

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
        self.resolution = gray.shape[::-1]

    def print_values(self):
        print 'total_error:\t\t' + str(self.total_error)
        print 'ret:\t\t\t' + str(self.ret)
        print 'mtx.shape:\t\t' + str(self.mtx.shape)
        print 'dist.shape:\t\t' + str(self.dist.shape)
        print 'rvecs.shape:\t\t' + str(np.shape(self.rvecs))
        print 'tvecs.shape:\t\t' + str(np.shape(self.tvecs))
        print 'np.shape(objpoints):\t' + str(np.shape(self.objpoints))
        print 'np.shape(imgpoints):\t' + str(np.shape(self.imgpoints))
        print 'resolution:\t\t' + str(self.resolution)
        print ''
##        print 'imgpoints2.shape:\t' + str(np.shape(imgpoints2))

##savefile = 'rgb_matrices.pkl'
##savefile = 'rgb_matrices_13_print.pkl'
##savefile = 'rgb_matrices_14_dual.pkl'
##savefile = '_matrices_12_ESS.pkl'
savefile = 'rgb_matrices_15_dual.pkl'
dill.load_session(savefile)
rgb = Matrices(total_error, ret, mtx, dist, rvecs, tvecs, imgpoints, objpoints, gray)
rgb.print_values()

##savefile = 'ir_matrices.pkl'
##savefile = 'ir_matrices_13_print.pkl'
##savefile = '_matrices_12_ESS.pkl'
savefile = 'ir_matrices_15_dual.pkl'
dill.load_session(savefile)
ir = Matrices(total_error, ret, mtx, dist, rvecs, tvecs, imgpoints, objpoints, gray)
ir.print_values()

##### find fundamental matrix F
####F, mask = cv2.findFundamentalMat(np.array(rgb.imgpoints[0]), np.array(ir.imgpoints[0]))
####print "F: " + str(F)
####print "mask.shape: " + str(mask.shape)
####print ''
####
##### uncalibrated stereo rectification
####ret, H1, H2 = cv2.stereoRectifyUncalibrated(rgb.imgpoints[0], ir.imgpoints[0], F, rgb.resolution)
####print "stereoRectifyUncalibrated ret: " + str(ret)
####print "H1: " + str(H1)
####print "H2: " + str(H2)
####
####R1 = np.linalg.inv(rgb.mtx)*H1*rgb.mtx
####R2 = np.linalg.inv(ir.mtx)*H2*ir.mtx
####P1 = rgb.mtx
####P2 = ir.mtx
####
####print "R1: " + str(R1)
####print "R2: " + str(R2)
####print "P1: " + str(P1)
####print "P2: " + str(P2)
####print ''

# mono calibration

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(rgb.objpoints, rgb.imgpoints, rgb.resolution, None, None)

# stereo calibration
flags = cv2.CALIB_FIX_ASPECT_RATIO + \
                    cv2.CALIB_ZERO_TANGENT_DIST + \
                    cv2.CALIB_USE_INTRINSIC_GUESS + \
                    cv2.CALIB_SAME_FOCAL_LENGTH + \
                    cv2.CALIB_RATIONAL_MODEL + \
                    cv2.CALIB_FIX_K3 + cv2.CALIB_FIX_K4 + cv2.CALIB_FIX_K5

##                    cv2.CALIB_USE_INTRINSIC_GUESS + \
##flags = None

criteria = (cv2.TERM_CRITERIA_COUNT + cv2.TERM_CRITERIA_EPS, 100, 0.00001)
##criteria = None

initCameraMatrix1 = cv2.initCameraMatrix2D(rgb.objpoints, rgb.imgpoints, rgb.resolution, 0);
initCameraMatrix2 = cv2.initCameraMatrix2D(ir.objpoints, ir.imgpoints, ir.resolution, 0);
initDist = np.array([[0]*5])
print "initCameraMatrix1: " + str(initCameraMatrix1)
print "initCameraMatrix2: " + str(initCameraMatrix2)
    
retval, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, R, T, E, F = cv2.stereoCalibrate(rgb.objpoints, rgb.imgpoints, ir.imgpoints, initCameraMatrix1, initDist, initCameraMatrix2, initDist, rgb.resolution, flags, criteria)

print "stereoCalibrate retval: " + str(retval)
print "cameraMatrix1: " + str(cameraMatrix1)
print "distCoeffs1: " + str(distCoeffs1)
print "cameraMatrix2: " + str(cameraMatrix2)
print "distCoeffs2: " + str(distCoeffs2)
print "R: " + str(R)
print "T: " + str(T)
print "E: " + str(E)
print "F: " + str(F)
print ''

# stereo rectification
flags = cv2.CALIB_ZERO_DISPARITY
##flags = None

R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, rgb.resolution, R, T, flags, 1, rgb.resolution)

print "R1: " + str(R1)
print "R2: " + str(R2)
print "P1: " + str(P1)
print "P2: " + str(P2)
print "Q: " + str(Q)
print "validPixROI1: " + str(validPixROI1)
print "validPixROI2: " + str(validPixROI2)
print ''

# undistort
rgb_mapx, rgb_mapy = cv2.initUndistortRectifyMap(cameraMatrix1, distCoeffs1, R1, P1, rgb.resolution, cv2.CV_32FC1) # 5
##rgb_mapx, rgb_mapy = cv2.initUndistortRectifyMap(rgb.mtx, rgb.dist, R1, P1, rgb.resolution, cv2.CV_32FC1) # 5
print "rgb_mapx.shape: " + str(rgb_mapx.shape)
print "rgb_mapy.shape: " + str(rgb_mapy.shape)
##rgb_path = 'C:/Users/d7rob/thesis/chess/master_set/rgb_7x6/img_2017-09-30_17-37-27.000_rgb_1_has_7x6_corners.jpg'
##rgb_path = 'C:/Users/d7rob/thesis/chess/master_set/rgb_7x6/img_2017-09-30_18-17-40.000_rgb_31_has_7x6_corners.jpg'
##rgb_path = 'C:/Users/d7rob/thesis/chess/20170923_174647.jpg'
##rgb_path = 'C:/Users/d7rob/thesis/chess/img1_2017-09-27_12-45-41.000_4.jpg'
rgb_path = 'C:/Users/d7rob/thesis/chess/rgb.jpg'
rgb_img = cv2.imread(rgb_path)
dst = cv2.remap(rgb_img, rgb_mapx, rgb_mapy, cv2.INTER_LINEAR)
k_crop = 1
h, w = rgb_img.shape[:2]
##dst2 = dst[(int)(h*(1-k_crop)):(int)(h*k_crop), (int)(w*(1-k_crop)):(int)(w*k_crop)]
##print "dst2.shape: " + str(dst2.shape)
rgb_undistort_path = rgb_path[:-4] + '_stereo_undistorted_1_15_light_rect.jpg'
print "rgb_undistort_path: " + str(rgb_undistort_path)
##cv2.rectangle(dst, validPixROI1[:2], validPixROI1[2:],(0, 0, 255),30)
dst = dst[validPixROI1[1]:validPixROI1[3], validPixROI1[0]:validPixROI1[2]]
cv2.imwrite(rgb_undistort_path, dst)

ir_mapx, ir_mapy = cv2.initUndistortRectifyMap(cameraMatrix2, distCoeffs2, R2, P2, ir.resolution, cv2.CV_32FC1) # 5
##ir_mapx, ir_mapy = cv2.initUndistortRectifyMap(ir.mtx, ir.dist, R2, P2, ir.resolution, cv2.CV_32FC1) # 5
print "ir_mapx.shape: " + str(ir_mapx.shape)
print "ir_mapy.shape: " + str(ir_mapy.shape)
##ir_path = 'C:/Users/d7rob/thesis/chess/master_set/ir_7x6/img_2017-09-30_18-17-40.000_ir_34_has_7x6_corners.jpg'
##ir_path = 'C:/Users/d7rob/thesis/chess/20170923_174647.jpg'
##ir_path = 'C:/Users/d7rob/thesis/chess/img1_2017-09-27_12-45-41.000_4.jpg'
ir_path = 'C:/Users/d7rob/thesis/chess/ir.jpg'
ir_img = cv2.imread(ir_path)
dst = cv2.remap(ir_img, ir_mapx, ir_mapy, cv2.INTER_LINEAR)
##k_crop = 1
##h, w = rgb_img.shape[:2]
##dst2 = dst[(int)(h*(1-k_crop)):(int)(h*k_crop), (int)(w*(1-k_crop)):(int)(w*k_crop)]
##print "dst2.shape: " + str(dst2.shape)
ir_undistort_path = ir_path[:-4] + '_stereo_undistorted_2_15_light_rect.jpg'
print "ir_undistort_path: " + str(ir_undistort_path)
##cv2.rectangle(dst, validPixROI2[:2], validPixROI2[2:],(0, 0, 255),30)
dst = dst[validPixROI2[1]:validPixROI2[3], validPixROI2[0]:validPixROI2[2]]
cv2.imwrite(ir_undistort_path, dst)

# mono output
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
print "newcameramtx: " + str(newcameramtx)
print "roi: " + str(roi)

# undistort
_mapx, _mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w,h), cv2.CV_32FC1) # 5
print "_mapx.shape: " + str(_mapx.shape)
print "_mapy.shape: " + str(_mapy.shape)
_path = rgb_path
_img = cv2.imread(_path)
_dst = cv2.remap(_img, _mapx, _mapy, cv2.INTER_LINEAR)

_undistort_path = _path[:-4] + '_stereo_undistorted_3_15_light.jpg'
print "_undistort_path: " + str(_undistort_path)
cv2.imwrite(_undistort_path, _dst)



