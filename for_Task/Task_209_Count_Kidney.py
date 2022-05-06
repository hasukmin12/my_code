import numpy as np # linear algebra
import skimage, os
import numpy as np
import cv2
import os
import nibabel as nib



path = '/home/has/Datasets/_has_Task128_Urinary'

path_list = next(os.walk(path))[1]
path_list.sort()
print(path_list)

total_kid_cnt = 0
total_blad_cnt = 0

for case in path_list[::-1]:

    print("")
    print("case : ", case)

    # img_path = os.path.join(path, case, 'imaging.nii.gz')
    seg_path = os.path.join(path,case,'segmentation.nii.gz')
    # img = nib.load(img_path).get_fdata()
    seg = nib.load(seg_path).get_fdata()
    # print(case)
    # print(seg.shape)


    z_axis = int(seg.shape[0])
    if len(np.where(seg==3)[0]) < 100:
        total_kid_cnt += 1

    if len(np.where(seg==2)[0]) < 100:
        total_blad_cnt += 1

    print("total_kid_cnt : ", total_kid_cnt)
    print("total_blad_cnt : ", total_blad_cnt)



print("total_kid_cnt : ", total_kid_cnt)
print("total_blad_cnt : ", total_blad_cnt)

print("actual kid value : ", 300 - total_kid_cnt)
print("actual blad value : ", 300 - total_blad_cnt)