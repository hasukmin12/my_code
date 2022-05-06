import nibabel as nib
import os
import numpy as np
import shutil


path = '/home/has/Datasets/_has_Task131_Bladder'
urinary_list = next(os.walk(path))[1]
urinary_list.sort()
# print(kid_blad_list)
print(urinary_list)



# for case in urinary_list:
#
#
#     urinary_path = os.path.join(path,case,'segmentation.nii.gz')
#     urinary_mask = nib.load(urinary_path).get_fdata()
#
#
#     if urinary_mask.max() != 1:
#         print(urinary_mask.max())
#         print(case)
#         print(urinary_path)



for case in urinary_list:


    urinary_path = os.path.join(path,case,'segmentation.nii.gz')
    img_path = os.path.join(path, case, 'imaging.nii.gz')

    urinary_mask = nib.load(urinary_path).get_fdata()
    img_mask = nib.load(img_path).get_fdata()


    if urinary_mask.shape != img_mask.shape:
        print(case)