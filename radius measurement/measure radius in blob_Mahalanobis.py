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
from scipy.spatial.distance import cdist
import os
import cv2
# from scipy.ndimage import distance_transform_edt as distance
from skimage import segmentation as skimage_seg
from scipy.spatial import distance



# path = '/home/has/Datasets/_has_ureter_overlap_rst/Ureter/Task_152 (DDense)_ch_colr/case_00291.nii.gz'
path = '/home/has/Results/inf_2_GT_295_CADD'
path_list = next(os.walk(path))[2]
path_list.sort()
print(path_list)

GT_path = '/home/has/Results/labelsTs'
GT_path_list = next(os.walk(path))[2]
GT_path_list.sort()
print(GT_path_list)

from PIL import Image
from PIL import ImageFilter
import scipy.spatial.distance as SSD
def Mahalanobis_distance(pred, gt):


    # M = np.array([pred.mean(), gt.mean()])  # means vector
    # covariance = np.cov([pred.ravel(), pred.ravel()])
    # inv_cov = np.linalg.inv(covariance)  # inv. covariance matrix
    #
    # def orig(A, B, M, inv_cov):
    #     h, w = A.shape
    #     result = np.zeros_like(A, dtype='float64')
    #
    #     for i in range(h):
    #         for j in range(w):
    #             # array with particular pixels from each image
    #             v = np.array([A[i, j], B[i, j]])
    #             # calculate mahalanobis distance and insert value as a pixel
    #             result[i, j] = SSD.mahalanobis(v, M, inv_cov)
    #     return result
    #
    # def using_cdist(A, B, M, inv_cov):
    #     D = np.dstack([A, B]).reshape(-1, 3)
    #     result = SSD.cdist(D, M[None, :], metric='mahalanobis', VI=inv_cov)
    #     result = result.reshape(A.shape)
    #     return result
    #
    # expected = orig(pred,gt, M, inv_cov)
    # result = using_cdist(pred,gt, M, inv_cov)
    # assert np.allclose(result, expected)
    #
    # print(result)






    #
    # xx = pred.T
    # yy = gt.T
    #
    # X = np.vstack([xx, yy])
    # V = np.cov(X.T)
    # VI = np.linalg.inv(V)
    # print(np.diag(np.sqrt(np.dot(np.dot((xx - yy), VI), (xx - yy).T))))
    #
    # results = cdist(xx, yy, 'mahalanobis')
    #
    # results = np.diag(results)
    # print(results)
    #
    # i, j = pred.shape
    # pred_x = pred.reshape(i, j).T
    #
    # i, j = gt.shape
    # gt_x = gt.reshape(i, j).T
    #
    # results = cdist(pred, gt, 'mahalanobis')






    dis = []
    kernel1d = cv2.getGaussianKernel(5,0.5)
    kernel2d = np.outer(kernel1d, kernel1d.transpose())
    u = np.zeros(gt.shape)

    # pt = np.where(gt!=0)
    # print(pt)
    filtered_gt = cv2.filter2D(gt, cv2.CV_32F, kernel2d)
    pt = np.where(filtered_gt == filtered_gt.max())
    # print(int(pt[1]))
    u_pt = np.array([int(pt[0]), int(pt[1])])
    u[int(pt[0])][int(pt[1])] = 1

    IV = filtered_gt.T




    # X = np.vstack([pred, gt])
    # V = np.cov(X.T)
    # VI = np.linalg.inv(V)
    # delta = pred - gt
    # results = np.sqrt(np.einsum('nj,jk,nk->n', delta, IV, delta))


    pred_list_form = np.where(pred == 1)
    # pred_list = []
    # for i in range(len(pred_list_form[0])):
    #     pred_list.append(np.array([int(pred_list_form[0][i]), int(pred_list_form[1][i])]))



    # 지티의 맥스값인 점, 분포의 역, 예측값의 점
    for i in range(len(pred_list_form)):
        a = np.zeros(pred.shape)
        a[int(pred_list_form[0][i])][int(pred_list_form[1][i])] = 1


        rst = (a-u)


        # rst = np.diag(np.sqrt(np.dot(np.dot((a - u), IV), (a - u).T)))
        dis.append(rst)



        # dis.append(distance.mahalanobis(a, u, IV))


    return np.mean(dis)


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
                distance_score.append(0)

            else:
                seg_l_img = np.array(seg_l, dtype=np.uint8)
                GT_l_img = np.array(GT_l, dtype=np.uint8)

                Mahalanobis_distance(seg_l_img[z], GT_l_img[z])
                # r1, blob1 = blob_detecter_2(GT_l_img[z])
                # r2, blob2 = blob_detecter_2(seg_l_img[z])


                # len_xy = ((blob1[0][0]-blob2[0][0])**2 + (blob1[0][1]-blob2[0][1])**2)**0.5
                # len_xy = len_xy.real
                #
                # #  원점간의 거리 <= GT의 반지름 (정답 슬라이스)
                # if (len_xy > (r1*2)):
                #     distance_score.append(0)
                # else:
                #     distance_score.append(1 - (len_xy/(r1*2)))


        # 우측 점
        if 1 in GT_r[z]:
            if 1 not in seg_r[z]:
                # print("non_L : ", z)
                distance_score.append(0)

        if 1 in seg_r[z]:
            if 1 not in GT_r[z]:
                distance_score.append(0)

            else:
                seg_r_img = np.array(seg_r, dtype=np.uint8)
                GT_r_img = np.array(GT_r, dtype=np.uint8)

                rst = Mahalanobis_distance(seg_r_img[z], GT_r_img[z])
                # r1, blob1 = blob_detecter_2(GT_r_img[z])
                # r2, blob2 = blob_detecter_2(seg_r_img[z])

                # len_xy = ((blob1[0][0] - blob2[0][0]) ** 2 + (blob1[0][1] - blob2[0][1]) ** 2) ** 0.5
                # len_xy = len_xy.real
                #
                # #  원점간의 거리 <= GT의 반지름 (정답 슬라이스)
                # if (len_xy > (r1*2)):
                #     distance_score.append(0)
                # else:
                #     distance_score.append(1 - (len_xy / (r1*2)))


    print("Distance Score : ", np.average(distance_score))
    easy_total_distance.append(np.average(distance_score))









#
#
#
# for i in hard_list:
#     case = path_list[i]
#     print()
#     print("hard : ", case)
#     seg_path = os.path.join(path, case)
#     seg = nib.load(seg_path).get_fdata()
#
#     GT_seg_path = os.path.join(GT_path, GT_path_list[path_list.index(case)])
#     GT = nib.load(GT_seg_path).get_fdata()
#
#     z_axis = int(seg.shape[0])
#
#     seg_l = seg[:, :256, :]
#     seg_r = seg[:, 256:, :]
#
#     GT_l = GT[:, :256, :]
#     GT_r = GT[:, 256:, :]
#
#     # plt.imshow(seg[z], cmap='bone')
#
#     distance_score = []
#
#     for z in range(0, z_axis):
#
#         # if z == 30:
#         #     print("debug")
#
#         if 1 in GT_l[z]:
#             if 1 not in seg_l[z]:
#                 # print("non_L : ", z)
#                 distance_score.append(0)
#
#         if 1 in seg_l[z]:
#             if 1 not in GT_l[z]:
#                 distance_score.append(0)
#
#             else:
#                 seg_l_img = np.array(seg_l, dtype=np.uint8)
#                 GT_l_img = np.array(GT_l, dtype=np.uint8)
#
#
#                 r1, blob1 = blob_detecter_2(GT_l_img[z])
#                 r2, blob2 = blob_detecter_2(seg_l_img[z])
#
#
#                 len_xy = ((blob1[0][0]-blob2[0][0])**2 + (blob1[0][1]-blob2[0][1])**2)**0.5
#                 len_xy = len_xy.real
#
#                 #  원점간의 거리 <= GT의 반지름 (정답 슬라이스)
#                 if (len_xy > (r1*2)):
#                     distance_score.append(0)
#                 else:
#                     distance_score.append(1 - (len_xy/(r1*2)))
#
#
#         # 우측 점
#         if 1 in GT_r[z]:
#             if 1 not in seg_r[z]:
#                 # print("non_L : ", z)
#                 distance_score.append(0)
#
#         if 1 in seg_r[z]:
#             if 1 not in GT_r[z]:
#                 distance_score.append(0)
#
#             else:
#                 seg_r_img = np.array(seg_r, dtype=np.uint8)
#                 GT_r_img = np.array(GT_r, dtype=np.uint8)
#
#                 r1, blob1 = blob_detecter_2(GT_r_img[z])
#                 r2, blob2 = blob_detecter_2(seg_r_img[z])
#
#                 len_xy = ((blob1[0][0] - blob2[0][0]) ** 2 + (blob1[0][1] - blob2[0][1]) ** 2) ** 0.5
#                 len_xy = len_xy.real
#
#                 #  원점간의 거리 <= GT의 반지름 (정답 슬라이스)
#                 if (len_xy > (r1*2)):
#                     distance_score.append(0)
#                 else:
#                     distance_score.append(1 - (len_xy / (r1*2)))
#
#     print("Distance Score : ", np.average(distance_score))
#     hard_total_distance.append(np.average(distance_score))



print()
print()
print("easy case total distance score : ", np.average(easy_total_distance))
print("hard case total distance score : ", np.average(hard_total_distance))

print()
total_distance = easy_total_distance + hard_total_distance
print("total ratio : ", np.average(total_distance))
print()
















