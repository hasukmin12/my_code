import nibabel as nib
import os
import numpy as np
import shutil


path = '/home/has/Datasets/_has_Task126_Urinary'
urinary_list = next(os.walk(path))[1]
urinary_list.sort()
# print(kid_blad_list)
# print(ureter_list)



print("----------strat with mask_1----------")
for case in urinary_list:

    urinary_path = os.path.join(path,case,'segmentation.nii.gz')
    urinary_mask = nib.load(urinary_path).get_fdata()

    mask_1 = np.where(urinary_mask==1)
    if mask_1[0].size == 0:
        print(case)


print("finish")
print("")
print("----------strat with mask_2-----------")
for case in urinary_list:

    urinary_path = os.path.join(path, case, 'segmentation.nii.gz')
    urinary_mask = nib.load(urinary_path).get_fdata()

    mask_2 = np.where(urinary_mask == 2)
    if mask_2[0].size == 0:
        print(case)



print("finish")
print("")
print("----------strat with mask_3----------")
for case in urinary_list:

    urinary_path = os.path.join(path, case, 'segmentation.nii.gz')
    urinary_mask = nib.load(urinary_path).get_fdata()

    mask_3 = np.where(urinary_mask == 3)
    if mask_3[0].size == 0:
        print(case)










