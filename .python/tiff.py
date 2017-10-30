import glob, cv2

dir = 'L:/Backups/thesis/Chris/0006'

images = glob.glob(dir + '/*.TIF')
print images

for i in images:
    img = cv2.imread(i, 2)
    print img
    cv2.imwrite(i[:-4] + '.jpg', img, )

