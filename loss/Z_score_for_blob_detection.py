import numpy as np
import os
import cv2
import copy
from PIL import Image
import nibabel as nib



# mask_2 = '/home/has/Datasets/CT_annotated/00138812 김영대 180517/Marked_nooverlay_png/00138812 김영대 180517 pre0042.png'
path = '/home/has/Results/inf_2_GT_130/case_00283.nii.gz'
mask = nib.load(path).get_fdata()

z_axis = int(mask.shape[0])
mask_1 = mask[32]


def blob_detecter(img):

    # cv2.imshow('img', img)
    # cv2.waitKey(0)

    img_gray = img.astype(np.uint8)


    # ret, img_binary = cv2.threshold(img_gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    blob = [[0,0],[0,0],[0,0]]


    for cnt in contours:

        M = cv2.moments(cnt)

        # print(M['m10'])
        # print("(M['m00'] : ", M['m00'])
        if M['m00']== 0.0:
            cx = 0.0
            cy = 0.0
        else:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])


        if blob[0] == [0, 0]:
            blob[0] = [cx, cy]
        elif blob[1 == [0,0]]:
            blob[1] = [cx, cy]
        else:
            blob[2] = [cx, cy]

    blob = np.array(blob)
    return blob


blob = blob_detecter(mask_1)

# print("")
# print("mask_1.max() : ",mask_1.max())
# print("blob[0] : ", blob[0])
# print("blob[1] : ",blob[1])
# print("blob[2] : ",blob[2])

if blob[0].max() == 0 and blob[1].max() == 0:
    print("zero")