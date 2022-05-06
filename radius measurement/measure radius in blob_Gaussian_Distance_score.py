import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from blob_detection_real.blob_detection_for_numpy import blob_detecter
from scipy.stats import wasserstein_distance
import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
# from blob_detection_real.blob_detection_for_numpy import blob_detecter
from PIL import Image
from scipy.spatial.distance import cdist
import os
import cv2
from scipy.ndimage import distance_transform_edt as distance
from skimage import segmentation as skimage_seg

# path = '/home/has/Datasets/_has_ureter_overlap_rst/Ureter/Task_152 (DDense)_ch_colr/case_00291.nii.gz'
path = '/home/has/Results/inf_2_GT_275_Res_no23'
path_list = next(os.walk(path))[2]
path_list.sort()
print(path_list)

GT_path = '/home/has/Results/labelsTs'
GT_path_list = next(os.walk(path))[2]
GT_path_list.sort()
print(GT_path_list)

from PIL import Image
from PIL import ImageFilter

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


def Gaussian_distance_score(pred, gt):

    # i, j = pred.shape
    # pred_x = pred.reshape(i, j).T
    #
    # i, j = gt.shape
    # gt_x = gt.reshape(i, j).T


    kernel1d = cv2.getGaussianKernel(5,0.5)
    kernel2d = np.outer(kernel1d, kernel1d.transpose())

    pt = np.where(gt!=0)
    pt_2 = np.where(pred!= 0)
    # print(pt)
    filtered_pred = cv2.filter2D(pred, cv2.CV_32F, kernel2d)
    filtered_gt = cv2.filter2D(gt, cv2.CV_32F, kernel2d)


    # if filtered_gt.max() > 1.0:
    #     radius, pt_pred = blob_detecter_2(gt)
    # if filtered_pred.max() > 1.0:
    #     r_p, pt_pred = blob_detecter_2(pred)

    ex_pt_gt = np.where(filtered_gt > 0.1)
    ex_pt_pred = np.where(filtered_pred > 0.1)

    # center of GT (pt_gt)
    pt_gt_list = np.where(filtered_gt == filtered_gt.max())
    if len(pt_gt_list[0]) == 1:
        pt_gt = np.array([int(pt_gt_list[0]), int(pt_gt_list[1])])
    else:
        stack_max = 0
        for i in range(len(pt_gt_list[0])):
            stack = 0
            if int(pt_gt_list[0][i] + 1) < 256:
                stack += filtered_gt[int(pt_gt_list[0][i]) + 1][int(pt_gt_list[1][i])]
                stack += filtered_gt[int(pt_gt_list[0][i]) + 1][int(pt_gt_list[1][i]) + 1]
                stack += filtered_gt[int(pt_gt_list[0][i])][int(pt_gt_list[1][i]) + 1]
            else:
                stack += filtered_gt[int(pt_gt_list[0][i]) - 1][int(pt_gt_list[1][i])]
                stack += filtered_gt[int(pt_gt_list[0][i]) - 1][int(pt_gt_list[1][i]) + 1]
                stack += filtered_gt[int(pt_gt_list[0][i])][int(pt_gt_list[1][i]) + 1]

            if stack_max<stack:
                stack_max = stack
                pt_gt = np.array([int(pt_gt_list[0][i]), int(pt_gt_list[1][i])])


    # center of Prediction (pt_pred)
    pt_pred_list = np.where(filtered_pred == filtered_pred.max())
    if len(pt_pred_list[0]) == 1:
        pt_pred = np.array([int(pt_pred_list[0]), int(pt_pred_list[1])])
    else:
        stack_max = 0
        for i in range(len(pt_pred_list[0])):
            stack = 0
            stack += filtered_pred[int(pt_pred_list[0][i]) + 1][int(pt_pred_list[1][i])]
            stack += filtered_pred[int(pt_pred_list[0][i]) + 1][int(pt_pred_list[1][i]) + 1]
            stack += filtered_pred[int(pt_pred_list[0][i])][int(pt_pred_list[1][i]) + 1]
            if stack_max < stack:
                stack_max = stack
                pt_pred = np.array([int(pt_pred_list[0][i]), int(pt_pred_list[1][i])])



    # calcuate distance between center (by Euclidean)
    len_xy = ((pt_gt[0] - pt_pred[0]) ** 2 + (pt_gt[1] - pt_pred[1]) ** 2) ** 0.5
    len_xy = len_xy.real



    # calcuate radius
    img = gt
    img_gray = img

    ret, img_binary = cv2.threshold(img_gray, 0.5, 255, 0)
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    r_list = []
    # for cnt in contours:
    # print(len(contours[0]))
    for i in range(len(contours[0])):
        tmp = contours[0][i][0]
        # print(tmp)
        r_list.append(((pt_gt[0] - tmp[1]) ** 2 + (pt_gt[1] - tmp[0]) ** 2) ** 0.5)

    radius = np.mean(r_list) * 2

    if len_xy > radius*2:
        rst = 0
        # print("len_xy > radius")
    else:
        rst = 1 - (len_xy/(radius*2))

    return rst


easy_total_distance = []
hard_total_distance = []


min = 1
max = 0

easy_list = [0,1,2,3,4,6,7,8,10,11,12,13,14,15,17,23,24,25,26,27,29,31,33,34,36,37,38,39,41,43,44,45,46,47,49,51,52,53,54,55,56,57,58,61,62,63,64,65,66,67,68]
hard_list = [5,9,16,18,19,20,21,22,28,30,32,35,42,48,50,59,60]
# weight = []


# for case in path_list:
for i in easy_list:
    case = path_list[i]
    print()
    print("easy : ", case)
    seg_path = os.path.join(path, case)
    seg = nib.load(seg_path).get_fdata()

    GT_seg_path = os.path.join(GT_path, GT_path_list[path_list.index(case)])
    GT = nib.load(GT_seg_path).get_fdata()

    z_axis = int(seg.shape[0])

    seg_l = seg[:, :256, :]
    seg_r = seg[:, 256:, :]

    GT_l = GT[:, :256, :]
    GT_r = GT[:, 256:, :]

    # plt.imshow(seg[z], cmap='bone')

    distance_score = []


    for z in range(0, z_axis):

        # if z == 30:
        #     print("debug")

        if 1 in GT_l[z]:
            if 1 not in seg_l[z]:
                # print("non_L : ", z)
                distance_score.append(0)

        if 1 in seg_l[z]:
            if 1 not in GT_l[z]:
                # print("non_L : ", z)
                distance_score.append(0)

            else:
                seg_l_img = np.array(seg_l, dtype=np.uint8)
                GT_l_img = np.array(GT_l, dtype=np.uint8)

                distance_score.append(Gaussian_distance_score(seg_l_img[z], GT_l_img[z]))
                # print("left : ", z,"    :" , Gaussian_distance_score(seg_l_img[z], GT_l_img[z]))



        # 우측 점
        if 1 in GT_r[z]:
            if 1 not in seg_r[z]:
                # print("non_L : ", z)
                distance_score.append(0)

        if 1 in seg_r[z]:
            if 1 not in GT_r[z]:
                # print("non_L : ", z)
                distance_score.append(0)

            else:
                seg_r_img = np.array(seg_r, dtype=np.uint8)
                GT_r_img = np.array(GT_r, dtype=np.uint8)

                distance_score.append(Gaussian_distance_score(seg_r_img[z], GT_r_img[z]))
                # print("right : ", z,"    :", Gaussian_distance_score(seg_r_img[z], GT_r_img[z]))


    print("Distance Score : ", np.average(distance_score))
    easy_total_distance.append(np.average(distance_score))







for i in hard_list:
    case = path_list[i]
    print()
    print("hard : ", case)
    seg_path = os.path.join(path, case)
    seg = nib.load(seg_path).get_fdata()

    GT_seg_path = os.path.join(GT_path, GT_path_list[path_list.index(case)])
    GT = nib.load(GT_seg_path).get_fdata()

    z_axis = int(seg.shape[0])

    seg_l = seg[:, :256, :]
    seg_r = seg[:, 256:, :]

    GT_l = GT[:, :256, :]
    GT_r = GT[:, 256:, :]

    # plt.imshow(seg[z], cmap='bone')

    distance_score = []


    for z in range(0, z_axis):

        # if z == 30:
        #     print("debug")

        if 1 in GT_l[z]:
            if 1 not in seg_l[z]:
                # print("non_L : ", z)
                distance_score.append(0)

        if 1 in seg_l[z]:
            if 1 not in GT_l[z]:
                # print("non_L : ", z)
                distance_score.append(0)

            else:
                seg_l_img = np.array(seg_l, dtype=np.uint8)
                GT_l_img = np.array(GT_l, dtype=np.uint8)

                distance_score.append(Gaussian_distance_score(seg_l_img[z], GT_l_img[z]))



        # 우측 점
        if 1 in GT_r[z]:
            if 1 not in seg_r[z]:
                # print("non_L : ", z)
                distance_score.append(0)

        if 1 in seg_r[z]:
            if 1 not in GT_r[z]:
                # print("non_L : ", z)
                distance_score.append(0)

            else:
                seg_r_img = np.array(seg_r, dtype=np.uint8)
                GT_r_img = np.array(GT_r, dtype=np.uint8)

                distance_score.append(Gaussian_distance_score(seg_r_img[z], GT_r_img[z]))


    print("Distance Score : ", np.average(distance_score))
    hard_total_distance.append(np.average(distance_score))



print()
print()
print("easy case total distance score : ", np.average(easy_total_distance))
print("hard case total distance score : ", np.average(hard_total_distance))

print()
total_distance = easy_total_distance + hard_total_distance
print("total ratio : ", np.average(total_distance))
print()

