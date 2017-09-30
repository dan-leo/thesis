import numpy as np
import dill

savefile = 'rgb_matrices.pkl'
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
