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

savefile = 'rgb_matrices.pkl'
dill.load_session(savefile)
rgb = Matrices(total_error, ret, mtx, dist, rvecs, tvecs, imgpoints, objpoints, gray)
rgb.print_values()

savefile = 'ir_matrices.pkl'
dill.load_session(savefile)
ir = Matrices(total_error, ret, mtx, dist, rvecs, tvecs, imgpoints, objpoints, gray)
ir.print_values()

# find fundamental matrix F
F, mask = cv2.findFundamentalMat(np.array(rgb.imgpoints[0]), np.array(ir.imgpoints[0]))
print "F: " + str(F)
print "mask.shape: " + str(mask.shape)
print ''

# uncalibrated stereo rectification
ret, H1, H2 = cv2.stereoRectifyUncalibrated(rgb.imgpoints[0], ir.imgpoints[0], F, rgb.resolution)
print "stereoRectifyUncalibrated ret: " + str(ret)
print "H1: " + str(H1)
print "H2: " + str(H2)

R1 = np.linalg.inv(rgb.mtx)*H1*rgb.mtx
R2 = np.linalg.inv(ir.mtx)*H2*ir.mtx
P1 = rgb.mtx
P2 = ir.mtx

print "R1: " + str(R1)
print "R2: " + str(R2)
print "P1: " + str(P1)
print "P2: " + str(P2)
print ''

# stereo calibration
flags = cv2.CALIB_FIX_ASPECT_RATIO + \
                    cv2.CALIB_ZERO_TANGENT_DIST + \
                    cv2.CALIB_USE_INTRINSIC_GUESS + \
                    cv2.CALIB_SAME_FOCAL_LENGTH + \
                    cv2.CALIB_RATIONAL_MODEL + \
                    cv2.CALIB_FIX_K3 + cv2.CALIB_FIX_K4 + cv2.CALIB_FIX_K5

retval, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, R, T, E, F = cv2.stereoCalibrate(rgb.objpoints, rgb.imgpoints, ir.imgpoints, rgb.mtx, rgb.dist, ir.mtx, ir.dist, rgb.resolution, flags)

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

R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, rgb.resolution, R, T, flags, 0, rgb.resolution)

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
print "rgb_mapx: " + str(rgb_mapx)
print "rgb_mapy: " + str(rgb_mapy)
##rgb_path = 'C:/Users/d7rob/thesis/chess/master_set/rgb_7x6/img_2017-09-30_17-37-27.000_rgb_1_has_7x6_corners.jpg'
rgb_path = 'C:/Users/d7rob/thesis/chess/master_set/rgb_7x6/img_2017-09-30_18-17-40.000_rgb_31_has_7x6_corners.jpg'
rgb_img = cv2.imread(rgb_path)
dst = cv2.remap(rgb_img, rgb_mapx, rgb_mapy, cv2.INTER_LINEAR)
k_crop = 1
h, w = rgb_img.shape[:2]
dst2 = dst[(int)(h*(1-k_crop)):(int)(h*k_crop), (int)(w*(1-k_crop)):(int)(w*k_crop)]
print "dst2.shape: " + str(dst2.shape)
rgb_undistort_path = rgb_path[:-4] + '_stereo_undistorted.jpg'
print "rgb_undistort_path: " + str(rgb_undistort_path)
cv2.imwrite(rgb_undistort_path, dst2)

ir_mapx, ir_mapy = cv2.initUndistortRectifyMap(cameraMatrix2, distCoeffs2, R2, P2, ir.resolution, cv2.CV_32FC1) # 5
print "ir_mapx: " + str(ir_mapx)
print "ir_mapy: " + str(ir_mapy)
ir_path = 'C:/Users/d7rob/thesis/chess/master_set/ir_7x6/img_2017-09-30_18-17-40.000_ir_34_has_7x6_corners.jpg'
ir_img = cv2.imread(ir_path)
dst = cv2.remap(ir_img, ir_mapx, ir_mapy, cv2.INTER_LINEAR)
k_crop = 1
h, w = rgb_img.shape[:2]
dst2 = dst[(int)(h*(1-k_crop)):(int)(h*k_crop), (int)(w*(1-k_crop)):(int)(w*k_crop)]
print "dst2.shape: " + str(dst2.shape)
ir_undistort_path = ir_path[:-4] + '_stereo_undistorted.jpg'
print "ir_undistort_path: " + str(ir_undistort_path)
cv2.imwrite(ir_undistort_path, dst2)


