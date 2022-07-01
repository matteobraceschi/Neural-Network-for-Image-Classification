import cv2
import glob
import os
import shutil

folderName = ['Apple', 'Blueberry', 'Cherry', 'Corn', 'Grape', 'Orange', 'Peach', 'Pepper', 'Potato', 'Raspberry', 'Soybean', 'Squash', 'Strawberry', 'Tomato']

if not os.path.exists('./validation'):
    os.mkdir('./validation')

for s in folderName:
    if not os.path.exists('./validation/'+s):
        os.mkdir('./validation/'+s)


    imgs = os.listdir('./training/'+s)

    for i in range(int(0.2*len(imgs))):
        shutil.move('./training/' +s+ '/'+imgs[i], './validation/'+s)



