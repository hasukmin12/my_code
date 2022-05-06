import os
import numpy as np
import nibabel as nib

# path = '/home/has/Datasets/_has_Task123_Ureter/case_00000/segmentation.nii.gz'
path = '/home/has/Results/CT_2_inference_rst_125_test_60/CT_242.nii.gz'
mask = nib.load(path).get_fdata()

z_axis = int(mask.shape[0])
# print(z_axis)
# print(mask.max())

cnt = 0
blank = 0

mask = mask.transpose(1,2,0)
print(mask.shape)

for z in range(0, z_axis):
    if mask[:,:,z].max() == 1:
        print(z)
        if mask[:,:,z + 1].max() == 0:
            continue

        cnt += 1
        sum = mask[:,:,z] + mask[:,:,z+1]
        # print(np.where(sum == 1)[0])
        num_1 = len(np.where(sum==1)[0])
        num_2 = len(np.where(sum == 2)[0])

        print(num_1)
        print(num_2)
        IoU = num_2 / (num_1 + num_2)
        if IoU < 0.3:
            blank += 1
            print("z axis : ", z)
            print("IoU is : ", IoU)
            print("")



if blank == 0:
    z_score = 0
else:
    z_score = blank / cnt

print("cnt : ", cnt)
print("blank : ", blank)
print("z_score : ", z_score)