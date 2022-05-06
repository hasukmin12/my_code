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


def cal_radius(img_1):
    # img = cv2.imread(img_1)
    # img_gt = img_1.astype(np.uint8)

    posmask = img_1.astype(np.bool)
    boundary = skimage_seg.find_boundaries(posmask, mode='inner').astype(np.uint8)
    # skimage_seg.active_contour()

    best_r = 0
    r = 0

    for y in range(0, 512):
        for x in range(0, 256):
            if boundary[x][y] == 1:
                i = 1
                while x+i<256 and boundary[x+i][y] == 1:
                    i += 1
                    r += 1
                if best_r < r :
                    best_r = r

    return best_r

    # x1 = 0
    # y1 = 0
    #
    # for y in range(0, 512):
    #     for x in range(0, 256):
    #         if boundary[x][y] == 1:
    #             i = 1
    #             while x+i<256 and boundary[x+i][y] == 1:
    #                 i += 1
    #                 r += 1
    #             if best_r < r :
    #                 best_r = r
    #                 x1 = x + (i/2)
    #                 y1 = y
    #
    #
    #
    # return best_r, x1, y1






# path = '/home/has/Datasets/_has_ureter_overlap_rst/Ureter/Task_152 (DDense)_ch_colr/case_00291.nii.gz'
path = '/home/has/Datasets/_has_Task220_Ureter_5mm'
path_list = next(os.walk(path))[1]
path_list.sort()
print(path_list)



total_ratio = 0
ratio_stack = 0
cnt_case = 0


print("")

radius_list = []

for case in path_list:
    case_path = os.path.join(path, case, 'segmentation.nii.gz')
    mask = nib.load(case_path).get_fdata()

    # mask = mask.transpose(2,0,1)
    z_axis = int(mask.shape[0])
    # print(mask.shape)

    total_cnt = 0
    cnt = 0

    mask_l = mask[:, :256, :]
    mask_r = mask[:, 256:, :]



    for z in range(0, z_axis):

        if mask[z].max() != 0:
            # print(z)
            total_cnt += 1

            mask_l_img = np.array(mask_l, dtype=np.uint8)
            mask_r_img = np.array(mask_r, dtype=np.uint8)
            # print(mask_l_img.max())
            # print(mask_r_img.max())

            mask_img = np.array(mask, dtype=np.uint8)

            # plt.figure("check", (12, 6))
            # plt.subplot(1, 2, 1)
            # plt.title("left")
            # plt.imshow(mask_l_img[z], cmap="gray")
            # plt.subplot(1, 2, 2)
            # plt.title("right")
            # plt.imshow(mask_r_img[z])
            # plt.show()

            rad_l = cal_radius(mask_l_img[z])
            rad_r = cal_radius(mask_r_img[z])

            radius_list.append(rad_l)
            radius_list.append(rad_r)

            # print(radius_list)


# plt.hist(radius_list, label='bins=10')
plt.hist(radius_list, bins=50, label='bins=50')
plt.legend()
plt.show()




