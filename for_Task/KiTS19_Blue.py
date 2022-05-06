import nibabel as nib
import os
import numpy as np
import shutil


path = '/home/has/Datasets/_has_KiTS19_blue'
urinary_list = next(os.walk(path))[1]
urinary_list.sort()
# print(kid_blad_list)
print(urinary_list)

aim_path = '/home/has/Datasets/_has_KiTS19_Blue'
if os.path.isdir(aim_path)==False:
    os.makedirs(aim_path)


for case in urinary_list:
    print(case)

    input = os.path.join(path,case,'segmentation.nii.gz')
    print(input)
    output = os.path.join(aim_path,'case_{0:05d}.nii.gz'.format(urinary_list.index(case)))
    print(output)

    shutil.copyfile(input,output)




