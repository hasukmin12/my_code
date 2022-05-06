import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from blob_detection_real.blob_detection_for_numpy import blob_detecter

import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
# from blob_detection_real.blob_detection_for_numpy import blob_detecter
from PIL import Image
import numpy as np
import os
import cv2
from scipy.ndimage import distance_transform_edt as distance
from skimage import segmentation as skimage_seg

# path = '/home/has/Datasets/_has_ureter_overlap_rst/Ureter/Task_152 (DDense)_ch_colr/case_00291.nii.gz'
path = '/home/has/Results/inf_2_GT_275_DDense'
path_list = next(os.walk(path))[2]
path_list.sort()
print(path_list)

GT_path = '/home/has/Results/labelsTs'
GT_path_list = next(os.walk(path))[2]
GT_path_list.sort()
print(GT_path_list)


def blob_detecter_2(img_1):

    img = img_1
    img_gray = img

    ret, img_binary = cv2.threshold(img_gray, 0.5, 255, 0)
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    blob1 = [[0, 0], [0, 0]]
    blob2 = [[0, 0], [0, 0]]
    radius = 0

    for cnt in contours:

        (x, y), radius = cv2.minEnclosingCircle(cnt)
        radius = int(radius)

        if blob1[0] == [0, 0]:
            blob1[0] = [x, y]
        else:
            blob1[1] = [x, y]

    blob1 = np.array(blob1)

    return radius*2, blob1


# total_ratio_e = 0
ratio_stack_e = 0
cnt_case_e = 0
ratio_stack_h = 0
cnt_case_h = 0

radius_list = []

min = 1
max = 0

easy_list = [0,1,2,3,4,6,7,8,10,11,12,13,14,15,17,23,24,25,26,27,29,31,33,34,36,37,38,39,41,43,44,45,46,47,49,51,52,53,54,55,56,57,58,61,62,63,64,65,66,67,68]
hard_list = [5,9,16,18,19,20,21,22,28,30,32,35,42,48,50,59,60]
# weight = []


# for case in path_list:
for i in easy_list[5:]:
    case = path_list[i]
    print()
    print("easy : ", case)
    cnt_case_e += 1
    seg_path = os.path.join(path, case)
    seg = nib.load(seg_path).get_fdata()


    GT_seg_path = os.path.join(GT_path, GT_path_list[path_list.index(case)])
    GT = nib.load(GT_seg_path).get_fdata()

    z_axis = int(seg.shape[0])

    total_cnt = 0
    cnt = 0

    seg_l = seg[:, :256, :]
    seg_r = seg[:, 256:, :]

    GT_l = GT[:, :256, :]
    GT_r = GT[:, 256:, :]

    # plt.imshow(seg[z], cmap='bone')



    for z in range(0, z_axis):

        # if z == 30:
        #     print("debug")

        if 1 in GT_l[z]:
            if 1 not in seg_l[z]:
                print("non_L : ", z)
                total_cnt += 1

        if 1 in seg_l[z]:
            # print(z)
            total_cnt += 1
            if 1 not in GT_l[z]:
                print("only pred L : ", z)
                # plt.imshow(seg_l[z])
                # plt.imshow(seg[z])
                # plt.show()


            else:
                seg_l_img = np.array(seg_l, dtype=np.uint8)
                GT_l_img = np.array(GT_l, dtype=np.uint8)


                r1, blob1 = blob_detecter_2(GT_l_img[z])
                r2, blob2 = blob_detecter_2(seg_l_img[z])


                # if blob1[1].max() != 0 or blob2[1].max() != 0:
                #     print("two blob L : ", z)
                #
                # else:

                len_xy = ((blob1[0][0]-blob2[0][0])**2 + (blob1[0][1]-blob2[0][1])**2)**0.5
                len_xy = len_xy.real

                #  원점간의 거리 <= GT의 반지름 (정답 슬라이스)
                if (len_xy <= r1):
                    cnt += 1
                else:
                    print("short distance L : ", z)


        # 우측 점
        if 1 in GT_r[z]:
            if 1 not in seg_r[z]:
                print("non_R : ", z)
                total_cnt += 1

        if 1 in seg_r[z]:
            # print(z)
            total_cnt += 1
            if 1 not in GT_r[z]:
                print("only pred R : ", z)
                # plt.imshow(seg_r[z])
                # plt.show()



            else:
                seg_r_img = np.array(seg_r, dtype=np.uint8)
                GT_r_img = np.array(GT_r, dtype=np.uint8)

                r1, blob1 = blob_detecter_2(GT_r_img[z])
                r2, blob2 = blob_detecter_2(seg_r_img[z])

                # if blob1[1].max() != 0 or blob2[1].max() != 0:
                #     print("two blob R : ", z)
                #
                # else:

                len_xy = ((blob1[0][0] - blob2[0][0]) ** 2 + (blob1[0][1] - blob2[0][1]) ** 2) ** 0.5
                len_xy = len_xy.real

                #  원점간의 거리 <= GT의 반지름 (정답 슬라이스)
                if (len_xy <= r1):
                    cnt += 1
                else:
                    print("short distance R : ", z)


    print(cnt)
    print(total_cnt)

    if max < cnt / total_cnt:
        max = cnt / total_cnt
    if min > cnt / total_cnt:
        min = cnt / total_cnt
    ratio_stack_e += cnt / total_cnt
    print("radius ratio : ", cnt / total_cnt)

for i in hard_list:
    case = path_list[i]
    print()
    print("hard : ", case)
    cnt_case_h += 1
    seg_path = os.path.join(path, case)
    seg = nib.load(seg_path).get_fdata()


    GT_seg_path = os.path.join(GT_path, GT_path_list[path_list.index(case)])
    GT = nib.load(GT_seg_path).get_fdata()

    z_axis = int(seg.shape[0])

    total_cnt = 0
    cnt = 0

    seg_l = seg[:, :256, :]
    seg_r = seg[:, 256:, :]

    GT_l = GT[:, :256, :]
    GT_r = GT[:, 256:, :]

    # plt.imshow(seg[z], cmap='bone')



    for z in range(0, z_axis):

        # if z == 30:
        #     print("debug")

        if 1 in GT_l[z]:
            if 1 not in seg_l[z]:
                print("non_L : ", z)
                total_cnt += 1

        if 1 in seg_l[z]:
            # print(z)
            total_cnt += 1
            if 1 not in GT_l[z]:
                print("only pred L : ", z)
                # plt.imshow(seg_l[z])
                # plt.imshow(seg[z])
                # plt.show()


            else:
                seg_l_img = np.array(seg_l, dtype=np.uint8)
                GT_l_img = np.array(GT_l, dtype=np.uint8)


                r1, blob1 = blob_detecter_2(GT_l_img[z])
                r2, blob2 = blob_detecter_2(seg_l_img[z])


                # if blob1[1].max() != 0 or blob2[1].max() != 0:
                #     print("two blob L : ", z)
                #
                # else:

                len_xy = ((blob1[0][0]-blob2[0][0])**2 + (blob1[0][1]-blob2[0][1])**2)**0.5
                len_xy = len_xy.real

                #  원점간의 거리 <= GT의 반지름 (정답 슬라이스)
                if (len_xy <= r1):
                    cnt += 1
                else:
                    print("short distance L : ", z)


        # 우측 점
        if 1 in GT_r[z]:
            if 1 not in seg_r[z]:
                print("non_R : ", z)
                total_cnt += 1

        if 1 in seg_r[z]:
            # print(z)
            total_cnt += 1
            if 1 not in GT_r[z]:
                print("only pred R : ", z)
                # plt.imshow(seg_r[z])
                # plt.show()



            else:
                seg_r_img = np.array(seg_r, dtype=np.uint8)
                GT_r_img = np.array(GT_r, dtype=np.uint8)

                r1, blob1 = blob_detecter_2(GT_r_img[z])
                r2, blob2 = blob_detecter_2(seg_r_img[z])

                # if blob1[1].max() != 0 or blob2[1].max() != 0:
                #     print("two blob R : ", z)
                #
                # else:

                len_xy = ((blob1[0][0] - blob2[0][0]) ** 2 + (blob1[0][1] - blob2[0][1]) ** 2) ** 0.5
                len_xy = len_xy.real

                #  원점간의 거리 <= GT의 반지름 (정답 슬라이스)
                if (len_xy <= r1):
                    cnt += 1
                else:
                    print("short distance R : ", z)

    if max < cnt / total_cnt:
        max = cnt / total_cnt
    if min > cnt / total_cnt:
        min = cnt / total_cnt
    ratio_stack_h += cnt / total_cnt
    print("radius ratio : ", cnt / total_cnt)


total_ratio_e = ratio_stack_e / cnt_case_e
print()
print()
print("easy case total ratio : ", total_ratio_e)

total_ratio_h = ratio_stack_h / cnt_case_h
print("hard case total ratio : ", total_ratio_h)

total_ratio = (ratio_stack_h + ratio_stack_e) / (cnt_case_h + cnt_case_e)
print("total ratio : ", total_ratio)
print()
print("min : ", min)
print("max : ", max)















