import numpy as np
import os
import nibabel as nib
import shutil


path = '/home/has/Datasets/_has_Task273_Urinary'
path_list = next(os.walk(path))[1]
path_list.sort()
print(path_list)
print()

list_u = []
list_b = []
list_k = []

for case in path_list:
    case_path = os.path.join(path, case, 'segmentation.nii.gz')
    seg = nib.load(case_path).get_fdata()
    z_axis = int(seg.shape[0])
    if 1 in seg:
        list_u.append(case)
    if 2 in seg:
        list_b.append(case)
    if 3 in seg:
        list_k.append(case)

print(list_u)
print(list_b)
print(list_k)
print()
print(len(list_u))
print(len(list_b))
print(len(list_k))



