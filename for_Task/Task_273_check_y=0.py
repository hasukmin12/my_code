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
    if seg.max() == 0:
        print(case)











