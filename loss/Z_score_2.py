import os
import numpy as np
import nibabel as nib
from loss.Z_score_for_blob_detection import blob_detecter
import cv2


# path = '/home/has/Datasets/_has_Task123_Ureter/case_00000/segmentation.nii.gz'
path = '/home/has/Results/inf_2_GT_130/case_00286.nii.gz'
mask = nib.load(path).get_fdata()

z_axis = int(mask.shape[0])
# print(z_axis)
# print(mask.max())

cnt = 0
blank = 0
Z_list = []

for z in range(0, z_axis):
    if mask[z].max() == 1:
        Z_list.append(z)

        blob = blob_detecter(mask[z])
        if blob[0].max() != 0 and blob[1].max() != 0:
            # print("two blob is exist")
            # print(z)
            # print(blob_detecter(mask[z]))
            # print("")
            if blob[2].max() != 0:
                blank += 1
                print("there is three points")
                # print(z)
                # print("")

            sum = mask[z] + mask[z + 1]
            num_1 = len(np.where(sum == 1)[0])
            num_2 = len(np.where(sum == 2)[0])
            # print(num_1)
            # print(num_2)
            IoU = num_2 / (num_1 + num_2)
            if IoU < 0.03:
                blank += 1
                print("z axis : ", z)
                print("IoU is : ", IoU)
                print("")

        else:
            print("z axis : ", z)
            print("there is no blob")
            print("")

            blank += 1

# first = Z_list[0]
# last = Z_list[-1]

cnt = int(Z_list[-1]) - int(Z_list[0])

if blank == 0:
    z_score = 0
else:
    z_score = (blank-1) / cnt

print("cnt : ", cnt)
print("blank : ", blank-1)
print("z_score : ", z_score)