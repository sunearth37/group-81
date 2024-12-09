import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True)
args = vars(ap.parse_args())

#set images
img = cv2.imread(args["image"])
imgRM = img.copy()
imgGM = img.copy()
imgBM = img.copy()
imgOR = img.copy()
imgOG = img.copy()
imgOB = img.copy()
imgRV = img.copy()

#color mask filter
imgRM[:,:,2] = 0
imgGM[:,:,1] = 0
imgBM[:,:,0] = 0
#only color filter
imgOR[:,:,0] = 0
imgOR[:,:,1] = 0
imgOG[:,:,0] = 0
imgOG[:,:,2] = 0
imgOB[:,:,1] = 0
imgOB[:,:,2] = 0
#None color filter
img16 = img.astype(np.uint16)
b,g,r = cv2.split(img16)
imgNC = ((b+g+r)/3).astype(np.uint8)
#Reverse color filter
imgRV[:,:,0] = 255 - imgRV[:,:,0]
imgRV[:,:,1] = 255 - imgRV[:,:,1]
imgRV[:,:,2] = 255 - imgRV[:,:,2]

#set images and titles by plots
fig, ax = plt.subplots(3,3, figsize = (20, 20))
ax[0, 0].imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
ax[0, 0].set_title('Original')
ax[0, 1].imshow(cv2.cvtColor(imgNC,cv2.COLOR_BGR2RGB))
ax[0, 1].set_title('None color')
ax[0, 2].imshow(cv2.cvtColor(imgRV,cv2.COLOR_BGR2RGB))
ax[0, 2].set_title('Reverse Color')
ax[1, 0].imshow(cv2.cvtColor(imgRM,cv2.COLOR_BGR2RGB))
ax[1, 0].set_title('Red Mask')
ax[1, 1].imshow(cv2.cvtColor(imgGM,cv2.COLOR_BGR2RGB))
ax[1, 1].set_title('Green Mask')
ax[1, 2].imshow(cv2.cvtColor(imgBM,cv2.COLOR_BGR2RGB))
ax[1, 2].set_title('Blue Mask')
ax[2, 0].imshow(cv2.cvtColor(imgOR,cv2.COLOR_BGR2RGB))
ax[2, 0].set_title('Only Red')
ax[2, 1].imshow(cv2.cvtColor(imgOG,cv2.COLOR_BGR2RGB))
ax[2, 1].set_title('Only Green')
ax[2, 2].imshow(cv2.cvtColor(imgOB,cv2.COLOR_BGR2RGB))
ax[2, 2].set_title('Only Blue')

#show plots
plt.show()
