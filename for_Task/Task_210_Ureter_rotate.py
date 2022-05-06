import numpy as np # linear algebra

import skimage, os
import numpy as np

import cv2

import os
import nibabel as nib



path = '/home/has/Datasets/_has_Task195_Ureter_1mm'

aim_path = '/home/has/Datasets/_has_Task211_Ureter_1mm'
if os.path.isdir(aim_path) == False:
    os.makedirs(aim_path)

path_list = next(os.walk(path))[1]
path_list.sort()
print(path_list)


for case in path_list:

    img_path = os.path.join(path, case, 'imaging.nii.gz')
    seg_path = os.path.join(path,case,'segmentation.nii.gz')
    img = nib.load(img_path).get_fdata()
    seg = nib.load(seg_path).get_fdata()
    print(case)
    print(img.shape)

    z_axis = int(img.shape[0])
    xSize = 512
    ySize = 512
    vol_numpy = np.zeros((z_axis, xSize, ySize))
    vol_numpy_seg = np.zeros((z_axis, xSize, ySize))


    for z in range(0, z_axis):
        for x in range(0, 512):
            for y in range(0, 512):
                vol_numpy[z][x][511-y] = img[z][x][y]

    for z in range(0, z_axis):
        for x in range(0, 512):
            for y in range(0, 512):
                vol_numpy_seg[z][x][511-y] = seg[z][x][y]

    print(vol_numpy.shape)


    img_dir = os.path.join(aim_path, case)
    if os.path.isdir(img_dir) == False:
        os.makedirs(img_dir)

    img_out = os.path.join(aim_path, case, 'imaging.nii.gz')
    seg_out = os.path.join(aim_path, case, 'segmentation.nii.gz')

    xform = np.eye(4) * 2
    img_Nifti = nib.nifti1.Nifti1Image(vol_numpy, xform)
    label_Nifti = nib.nifti1.Nifti1Image(vol_numpy_seg, xform)

    nib.save(img_Nifti, img_out)
    nib.save(label_Nifti, seg_out)
    print("saved")
    print("")

