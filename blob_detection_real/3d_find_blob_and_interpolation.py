import numpy as np
from scipy.interpolate import interpn
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import scipy.misc
from glob import glob
import os
import nibabel as nib
import cv2
import copy



mask_1 = '/home/has/Datasets/CT_annotated/00138812 김영대 180517/Marked_nooverlay_png/00138812 김영대 180517 pre0042.png'
mask_2 = '/home/has/Datasets/CT_annotated/00138812 김영대 180517/Marked_nooverlay_png/00138812 김영대 180517 pre0047.png'

img = cv2.imread(mask_1)
img2 = cv2.imread(mask_2)



# cv2.imwrite('color_img.jpg', img)
# cv2.imshow("image", img)
# cv2.waitKey()


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_binary = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

blob1 = [[0,0],[0,0]]
blob2 = [[0,0],[0,0]]

for cnt in contours:

    M = cv2.moments(cnt)

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    cv2.circle(img, (cx, cy), 10, (0,0,255), -1)

    print(cx, cy)
    if blob1[0] == [0, 0]:
        blob1[0] = [cx, cy]
    else:
        blob1[1] = [cx, cy]

print(blob1)



img_gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret2, img_binary2 = cv2.threshold(img_gray2, 127, 255, 0)
contours2, hierarchy2 = cv2.findContours(img_binary2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for cnt2 in contours2:

    M = cv2.moments(cnt2)

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    cv2.circle(img2, (cx, cy), 10, (0,0,255), -1)

    print(cx, cy)
    if blob2[0] == [0,0]:
        blob2[0] = [cx,cy]
    else:
        blob2[1] = [cx,cy]


print(blob2)

img_list = [img_gray, img_gray2]

blob1 = np.array(blob1)
blob2 = np.array(blob2)



from scipy.ndimage.measurements import center_of_mass
from scipy.ndimage.interpolation import shift
import matplotlib.cm as cm

def inter(images,t):
#input:
# images: list of arrays/frames ordered according to motion
# t: parameter ranging from 0 to 1 corresponding to first and last frame
#returns: interpolated image

#direction of movement, assumed to be approx. linear
    a1 = blob1[0]
    a2 = blob1[1]

    b1 = blob2[0]
    b2 = blob2[1]

    # left interpolation
    #find index of two nearest frames
    arr_left = np.array([a1, b1])
    v_l = a1+t*(b1-a1) #conver t into vector
    idx1_l =(np.linalg.norm((arr_left - v_l),axis=1)).argmin()
    arr_left[idx1_l]=np.array([0,0]) #this is sloppy, should be changed if relevant values are near [0,0]
    idx2_l =(np.linalg.norm((arr_left - v_l),axis=1)).argmin()

    left_img = copy.deepcopy(img_list)
    right_img = copy.deepcopy(img_list)

    # img_copy1 = img_list[0]
    # img_copy2 = img_list[1]
    # right_img = [img_copy1,img_copy2]

    # ex = '/home/has/Datasets/1024ex.jpg'
    # ex_1024 = cv2.imread(ex)
    # img_ex = [ex_1024,img_]

    # cv2.imshow("image", img_list[1])
    # cv2.waitKey()


    for img in left_img:
        for i in range(0, 1024):
            for j in range(512, 1024):
                    img[i][j] = 0

    for img in right_img:
        for i in range(0, 1024):
            for j in range(0, 512):
                    img[i][j] = 0


    cv2.imshow("image", left_img[0])
    cv2.waitKey()


    if idx1_l > idx2_l:

        tstar = np.linalg.norm(v_l - a1) / np.linalg.norm(b1 - a1)  # define parameter ranging from 0 to 1 for interpolation between two nearest frames
        im1_shift = shift(left_img[idx2_l], (b1 - a1) * tstar)  # shift frame 1
        im2_shift = shift(left_img[idx1_l], -(b1 - a1) * (1 - tstar))  # shift frame 2
        rst = im1_shift + im2_shift

        return rst  # return average

    if idx1_l < idx2_l:
        tstar=np.linalg.norm(v_l-a1)/np.linalg.norm(b1-a1)
        im1_shift=shift(left_img[idx2_l],-(b1-a1)*(1-tstar))
        im2_shift=shift(left_img[idx1_l],(b1-a1)*(tstar))
        rst = im1_shift + im2_shift

        return rst






    # right interpolation
    #find index of two nearest frames
    arr_right = np.array([a2, b2])
    v_r = a2+t*(b2-a2) #conver t into vector
    idx1_r =(np.linalg.norm((arr_right - v_r),axis=1)).argmin()
    arr_right[idx1_r]=np.array([0,0]) #this is sloppy, should be changed if relevant values are near [0,0]
    idx2_r =(np.linalg.norm((arr_right - v_r),axis=1)).argmin()


    if idx1_r > idx2_r:

        tstar = np.linalg.norm(v_r - a2) / np.linalg.norm(b2 - a2)  # define parameter ranging from 0 to 1 for interpolation between two nearest frames
        im1_shift = shift(right_img[idx2_r], (b2 - a2) * tstar)  # shift frame 1
        im2_shift = shift(right_img[idx1_r], -(b2 - a2) * (1 - tstar))  # shift frame 2
        rst = im1_shift + im2_shift

        return rst  # return average

    if idx1_r < idx2_r:
        tstar=np.linalg.norm(v_r-a2)/np.linalg.norm(b2-a2)
        im1_shift=shift(right_img[idx2_r],-(b2-a2)*(1-tstar))
        im2_shift=shift(right_img[idx1_r],(b2-a2)*(tstar))
        rst = im1_shift + im2_shift

        return rst

#
#
#
#
#
#
out_1 = inter(img_list,0.2)

cv2.imwrite('0.2shift_ureter.png', out_1)
print("img saved")

cv2.imshow("image", out_1)
cv2.waitKey()
