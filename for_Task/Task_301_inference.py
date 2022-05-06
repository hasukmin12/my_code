import numpy as np
import os
import nibabel as nib
import shutil
join = os.path.join

path = '/home/has/Datasets/_has_KiPA'
path_list = next(os.walk(path))[1]
path_list.sort()
print(path_list)
print()


aim_path = '/home/has/Datasets/CT_2_inference_KiPA'
if os.path.isdir(aim_path)== False:
    os.makedirs(aim_path)

for case in path_list[50:]:
    name = "CT_{0:03d}_0000.nii.gz".format(int(path_list.index(case)))
    input = os.path.join(path, case, 'imaging.nii.gz')
    output = os.path.join(aim_path, name)


    shutil.copyfile(input, output)


