import glob, cv2
import numpy as np
from matplotlib import pyplot as plt

##images = glob.glob('L:/Backups/thesis/chess/rgb/compressed2/picked/*.jpg')
root_dir = 'C:/Users/d7rob/thesis/chess/13_print/compressed/picked'
images = glob.glob(root_dir + '/*.jpg')
print images

for fname in images:
    img = cv2.imread(fname)

    ##gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ##gray = img

    ##plt.imshow(gray)
    ##plt.show()

    ##cv2.imshow('gray', gray)
    ##cv2.waitKey(500)
    ##cv2.destroyAllWindows()

    flags = cv2.CALIB_CB_ADAPTIVE_THRESH + \
            cv2.CALIB_CB_NORMALIZE_IMAGE + \
            cv2.CALIB_CB_FILTER_QUADS + \
            cv2.CALIB_CB_FAST_CHECK
##    flags = cv2.CALIB_CB_FAST_CHECK
    ##flags = None
    # 7, 6
    ret, corners = cv2.findChessboardCorners(gray, (15,15), flags)

    print np.shape(corners), ret

    if ret == True:
        cv2.imwrite((str(fname[:-4]) + '_has_15x15_corners.jpg'), img)
    

