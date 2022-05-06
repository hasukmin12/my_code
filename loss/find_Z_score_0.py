import os
import numpy as np
import nibabel as nib
from loss.Z_score_for_blob_detection import blob_detecter
import cv2


# path = '/home/has/Datasets/_has_Task123_Ureter/case_00000/segmentation.nii.gz'
path = '/home/has/Results/inf_2_GT_130'
path_list = next(os.walk(path))[2]
path_list.sort()

min_z = 1
max_z = 0

for case in path_list:

    case_path = os.path.join(path,case)
    mask = nib.load(case_path).get_fdata()

    z_axis = int(mask.shape[0])
    # print(z_axis)
    # print(mask.max())

    cnt = 0
    blank = 0

    for z in range(0, z_axis):
        if mask[z].max() == 1:
            if mask[z + 1].max() == 0:
                continue

            cnt += 1
            blob = blob_detecter(mask[z])
            if blob[0].max() != 0 and blob[1].max() != 0:
                # print("two blob is exist")
                # print(z)
                # print(blob_detecter(mask[z]))
                # print("")
                if blob[2].max() != 0:
                    print("there is three points")
                    blank += 1
                    print(case)
                    print(z)
                    print("")

                sum = mask[z] + mask[z + 1]
                num_1 = len(np.where(sum == 1)[0])
                num_2 = len(np.where(sum == 2)[0])
                # print(num_1)
                # print(num_2)
                IoU = num_2 / (num_1 + num_2)
                if IoU < 0.1:
                    blank += 1
                    # print("z axis : ", z)
                    # print("IoU is : ", IoU)
                    # print("")

            else:
                # print("z axis : ", z)
                # print("there is no blob")
                # print("")

                blank += 1


    if blank == 0:
        z_score = 0
    else:
        z_score = blank / cnt



    # print("")
    # print("z_score : ",z_score)
    if z_score == 0:
        print(case)

    # print("cnt : ", cnt)
    # print("blank : ", blank)
    # print("z_score : ", z_score)