import os
import numpy as np
import nibabel as nib

path = '/home/has/Datasets/_has_ureter_overlap_rst/Ureter/Task_274_t69'
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
    for z in range(0, z_axis):

        if mask[z].max() != 0:
            # print(z)
            total_cnt += 1
            num_GT = len(np.where(mask[z] == 1)[0])
            num_pred = len(np.where(mask[z] == 2)[0])
            num_overlab = len(np.where(mask[z] == 4)[0])

            # print(num_GT)
            IoU = num_overlab / (num_GT + num_pred + num_overlab)
            # print(IoU)

            if IoU < 0.1:
                # print("z axis : ", z)
                # print("IoU is : ", IoU)
                # print("")
                cnt +=1

    ratio_stack += cnt / total_cnt
    print("30% ratio : ", 1 - ratio_stack)
    total_ratio = ratio_stack / cnt_case
    print("total ratio : ", 1 - total_ratio)

