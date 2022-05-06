
import skimage, os
import shutil
import numpy as np

import cv2
try:
    import nibabel as nib
except:
    raise ImportError('Install NIBABEL')



input_path = '/home/has/Results/inf_2_GT_221'
input_list = next(os.walk(input_path))[2]
input_list.sort()
print(input_list)

aim_path = '/home/has/Results/inf_2_GT_221_color_LR'
if os.path.isdir(aim_path) == False:
    os.makedirs(aim_path)



for case in input_list:
    print("")
    print(case)

    seg_path = os.path.join(input_path, case)
    seg = nib.load(seg_path).get_fdata()

    # seg = seg.transpose(2,0,1)
    print(seg.shape)

    z_axis = int(seg.shape[0])

    z_list = []


    for z in range(0, z_axis):
        for x in range(256, 512):
            for y in range(0, 512):
                if seg[z][x][y] == 1:
                    seg[z][x][y] = 2







    xform = np.eye(4) * 2
    seg_Nifti = nib.nifti1.Nifti1Image(seg, xform)
    output_path_seg = os.path.join(aim_path, case)
    print(seg_path)
    print(output_path_seg)
    nib.save(seg_Nifti, output_path_seg)




