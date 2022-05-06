import numpy as np
import os
import nibabel as nib
import shutil


path = '/home/has/Datasets/_has_Task295_Ureter'
path_list = next(os.walk(path))[1]
path_list.sort()
print(path_list)
print()


for case in path_list:
    # print()
    # print(case)
    case_path = os.path.join(path, case, 'segmentation.nii.gz')
    seg = nib.load(case_path).get_fdata()
    z_axis = int(seg.shape[0])

    if 1 not in seg:
        print(case)
        print("no 1")
        print()

    if 2 in seg:
        print(case)
        print("2 in case")
        print()

    if 3 in seg:
        print(case)
        print("3 in case")
        print()









