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

easy_list = [0,1,2,3,4,6,7,8,10,11,12,13,14,15,17,23,24,25,26,27,29,31,33,34,36,37,38,39,41,43,44,45,46,47,49,51,52,53,54,55,56,57,58,61,62,63,64,65,66,67,68]
hard_list = [5,9,16,18,19,20,21,22,28,30,32,35,42,48,50,59,60]

easy_score = []
hard_score = []

min = 1
max = 0

print("easy_case")
for i in hard_list:
    print("")
    case = path_list[i]
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

    if max < 1 - (cnt / total_cnt):
        max = 1 - (cnt / total_cnt)
    if min > 1 - (cnt / total_cnt):
        min = 1 - (cnt / total_cnt)
    ratio_stack += 1 - (cnt / total_cnt)
    print("30% ratio : ", 1 - cnt / total_cnt)
    total_ratio = ratio_stack / cnt_case
    print("total ratio : ", total_ratio)
    print("max : ", max)
    print("min : ", min)

