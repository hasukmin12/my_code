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
def sliced_wasserstein(X, Y, num_proj):
    dim = X.shape[1]
    ests = []
    for _ in range(num_proj):
        # sample uniformly from the unit sphere
        dir = np.random.rand(dim)
        dir /= np.linalg.norm(dir)

        # project the data
        X_proj = X @ dir
        Y_proj = Y @ dir

        # compute 1d wasserstein
        ests.append(wasserstein_distance(X_proj, Y_proj))
    return np.mean(ests)


def KLdivergence(x, y):
  """Compute the Kullback-Leibler divergence between two multivariate samples.
  Parameters
  ----------
  x : 2D array (n,d)
    Samples from distribution P, which typically represents the true
    distribution.
  y : 2D array (m,d)
    Samples from distribution Q, which typically represents the approximate
    distribution.
  Returns
  -------
  out : float
    The estimated Kullback-Leibler divergence D(P||Q).
  References
  ----------
  Pérez-Cruz, F. Kullback-Leibler divergence estimation of
continuous distributions IEEE International Symposium on Information
Theory, 2008.
  """
  from scipy.spatial import cKDTree as KDTree

  # Check the dimensions are consistent
  x = np.atleast_2d(x)
  y = np.atleast_2d(y)

  n,d = x.shape
  m,dy = y.shape

  assert(d == dy)


  # Build a KD tree representation of the samples and find the nearest neighbour
  # of each point in x.
  xtree = KDTree(x)
  ytree = KDTree(y)

  # Get the first two nearest neighbours for x, since the closest one is the
  # sample itself.
  r = xtree.query(x, k=2, eps=.01, p=2)[0][:,1]
  s = ytree.query(x, k=1, eps=.01, p=2)[0]

  # There is a mistake in the paper. In Eq. 14, the right side misses a negative sign
  # on the first term of the right hand side.
  return -np.log(r/s).sum() * d / n + np.log(m / (n - 1.))


def Mahalanobis_distance(pred, gt):

    # i, j = pred.shape
    # pred_x = pred.reshape(i, j).T
    #
    # i, j = gt.shape
    # gt_x = gt.reshape(i, j).T


    kernel1d = cv2.getGaussianKernel(5,0.5)
    kernel2d = np.outer(kernel1d, kernel1d.transpose())

    pt = np.where(gt!=0)
    print(pt)
    filtered_pred = cv2.filter2D(pred, cv2.CV_32F, kernel2d)
    filtered_gt = cv2.filter2D(gt, cv2.CV_32F, kernel2d)

    rst = KLdivergence(filtered_gt, filtered_pred)




    # ex = wasserstein_distance([[0, 1, 3],[2, 3, 4]], [[5, 6, 8],[5,6,7]])
    dis = sliced_wasserstein(filtered_pred, filtered_gt, 2)

    return dis


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
                print("non_L : ", z)
                # distance_score.append(0)

        if 1 in seg_l[z]:
            if 1 not in GT_l[z]:
                print("non_L : ", z)
                # distance_score.append(0)

            else:
                seg_l_img = np.array(seg_l, dtype=np.uint8)
                GT_l_img = np.array(GT_l, dtype=np.uint8)

                distance_score.append(Mahalanobis_distance(seg_l_img[z], GT_l_img[z]))
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
                print("non_L : ", z)
                # distance_score.append(0)

        if 1 in seg_r[z]:
            if 1 not in GT_r[z]:
                print("non_L : ", z)
                # distance_score.append(0)

            else:
                seg_r_img = np.array(seg_r, dtype=np.uint8)
                GT_r_img = np.array(GT_r, dtype=np.uint8)

                distance_score.append(Mahalanobis_distance(seg_r_img[z], GT_r_img[z]))
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

