import nibabel as nib
import os
import numpy as np
import shutil


path = '/home/has/Datasets/kits19/data'
urinary_list = next(os.walk(path))[1]
urinary_list.sort()
# print(kid_blad_list)
print(urinary_list)

aim_path = '/home/has/Datasets/CT_2_inference8_KiTS'
if os.path.isdir(aim_path) == False:
    os.makedirs(aim_path)



for case in urinary_list:
    print(case)

    input = os.path.join(path,case,'imaging.nii.gz')
    print(input)
    output = os.path.join(aim_path,'CT_{0:03d}_0000.nii.gz'.format(urinary_list.index(case)))
    print(output)

    shutil.copyfile(input,output)






