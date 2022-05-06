import numpy as np # linear algebra

import skimage, os
import numpy as np

import cv2

import os
import nibabel as nib


# path = '/home/has/Datasets/CT_2_inference6_test_69'

path = '/home/has/Datasets/ureter_overlap_rst/Ureter/Task_205_t69'

aim_path = '/home/has/Datasets/seg'
if os.path.isdir(aim_path) == False:
    os.makedirs(aim_path)

path_list = next(os.walk(path))[2]
path_list.sort()
print(path_list)


for case in path_list:

    img_path = os.path.join(path, case)
    img = nib.load(img_path).get_fdata()
    print(case)
    print(img.shape)

    z_axis = int(img.shape[0])
    xSize = 512
    ySize = 512
    vol_numpy = np.zeros((z_axis, xSize, ySize))


    for z in range(0, z_axis):
        for x in range(0, 512):
            for y in range(0, 512):
                vol_numpy[z][x][511-y] = img[z][x][y]

    print(vol_numpy.shape)
    img_out = os.path.join(aim_path,case)

    xform = np.eye(4) * 2
    img_Nifti = nib.nifti1.Nifti1Image(vol_numpy, xform)

    nib.save(img_Nifti, img_out)
    print("saved")
    print("")

