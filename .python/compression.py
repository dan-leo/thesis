import cv2
import glob

images = glob.glob('C:/Users/d7rob/thesis/chess/rgb/*.jpg')

for fname in images:
    print fname[:-4] + '_c.jpg'
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(fname[:-4] + '_c.jpg', gray,  [cv2.IMWRITE_PNG_COMPRESSION, 9])
    break
