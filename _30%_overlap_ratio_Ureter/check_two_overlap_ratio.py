import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from blob_detection_real.blob_detection_for_numpy import blob_detecter
from PIL import Image

path = '/home/has/Datasets/_has_ureter_overlap_rst/Ureter/Task_130 (UNet)_ch_colr'
path_list = next(os.walk(path))[2]
path_list.sort()
print(path_list)

total_ratio = 0
ratio_stack = 0
cnt_case = 0

for case in path_list:
    print("")
    print(case)
    cnt_case += 1
    case_path = os.path.join(path,case)
    mask = nib.load(case_path).get_fdata()

    mask = mask.transpose(2,0,1)
    z_axis = int(mask.shape[0])
    # print(mask.shape)

    total_cnt = 0
    cnt = 0

    mask_l = mask[:, :256, :]
    mask_r = mask[:, 256:, :]
    # print(mask_l.shape)
    # print(mask_r.shape)
    # plt.figure("check", (12, 6))
    # plt.subplot(1, 2, 1)
    # plt.title("image")
    # plt.imshow(mask_l[40, :, :], cmap="gray")
    # plt.subplot(1, 2, 2)
    # plt.title("label")
    # plt.imshow(mask_r[40, :, :])
    # plt.show()

    for z in range(0, z_axis):

        if mask[z].max() != 0:
            # print(z)
            total_cnt += 1

            mask_l_img = np.array(mask_l, dtype=np.uint8)
            mask_r_img = np.array(mask_r, dtype=np.uint8)

            blob_l = blob_detecter(mask_l_img[z])
            blob_r = blob_detecter(mask_r_img[z])

            if len(blob_l) != 1 or len(blob_r) != 1: # 한쪽에 2개 blob이 생기는 현상을 방지

                # left ureter
                num_GT_l = len(np.where(mask_l[z] == 1)[0])
                num_pred_l = len(np.where(mask_l[z] == 2)[0])
                num_overlab_l = len(np.where(mask_l[z] == 4)[0])

                # print(num_GT)
                if num_GT_l == 0:
                    IoU_l = 1
                else:
                    IoU_l = num_overlab_l / (num_GT_l + num_pred_l + num_overlab_l)


                # right ureter
                num_GT_r = len(np.where(mask_r[z] == 1)[0])
                num_pred_r = len(np.where(mask_r[z] == 2)[0])
                num_overlab_r = len(np.where(mask_r[z] == 4)[0])

                # print(num_GT)
                if num_GT_r == 0:
                    IoU_r = 1
                else:
                    IoU_r = num_overlab_r / (num_GT_r + num_pred_r + num_overlab_r)



                if 0.025 < IoU_l < 0.035 or 0.025< IoU_r <0.035:
                    print("z axis : ", z+1)
                    print("IoU_l is : ", IoU_r)
                    print("IoU_r is : ", IoU_l)
                    print("")
                    cnt +=1

                # if IoU_l < 0.03 or IoU_r <0.03:
                #     print("z axis : ", z+1)
                #     print("IoU_l is : ", IoU_l)
                #     print("IoU_r is : ", IoU_r)
                #     print("")
                #     cnt +=1

    # ratio_stack += cnt / total_cnt
    # print("30% ratio : ", 1 - ratio_stack)
    # total_ratio = ratio_stack / cnt_case
    # print("total ratio : ", 1 - total_ratio)

