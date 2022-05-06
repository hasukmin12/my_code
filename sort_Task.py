import numpy as np # linear algebra

import skimage, os
import numpy as np

import cv2

import os
import nibabel as nib

# path = '/home/has/Datasets/kits19/data'
path = '/home/has/Datasets/_has_Task100_Bladder'

path_list = next(os.walk(path))[1]
path_list.sort()

print(path_list)

aim_path ='/home/has/Datasets/Ureter_CT_img(reverse)'
if os.path.isdir(aim_path)==False:
    os.makedirs(aim_path)


for case in path_list:
    img_path = os.path.join(path, case, 'imaging.nii.gz')
    img = nib.load(img_path).get_fdata()
    print(case)


    xform = np.eye(4) * 2
    img_Nifti = nib.nifti1.Nifti1Image(img, xform)

    aim_name = case + ".nii.gz"
    aim_path_2 = os.path.join(aim_path,aim_name)

    nib.save(img_Nifti, aim_path_2)
    #nib.save(label_Nifti, seg_out)

