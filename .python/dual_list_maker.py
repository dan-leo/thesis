import glob

root_dir = 'C:/Users/d7rob/thesis/distorted/undistorted'
root_dir = 'L:/Backups/thesis/longridge'
root_dir = 'C:/Users/d7rob/thesis/home_lab_window_2'
root_dir = 'C:/Users/d7rob/thesis/home_lab_window_3/_noir'
root_dir = 'C:/Users/d7rob/thesis/chris'
root_dir = 'L:/Backups/thesis/heldervue'

_rgb_name = "/rgb_undistorted"
_ir_name = "/ir_undistorted"
rgb_images = glob.glob(root_dir + _rgb_name + '/*.jpg')
ir_images = glob.glob(root_dir + _ir_name + '/*.jpg')

for x, y in zip(rgb_images, ir_images):
    print y + ', ' + x
