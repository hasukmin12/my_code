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
    print()
    print(case)
    case_path = os.path.join(path, case, 'segmentation.nii.gz')
    seg = nib.load(case_path).get_fdata()
    z_axis = int(seg.shape[0])

    for z in range(0, z_axis):
        for x in range(0, 512):
            for y in range(0, 512):
                if seg[z][x][y] == 2:
                    seg[z][x][y] = 0
                elif seg[z][x][y] == 3:
                    seg[z][x][y] = 0

    xform = np.eye(4) * 2
    img_Nifti = nib.nifti1.Nifti1Image(seg, xform)
    nib.save(img_Nifti, case_path)
    print("saved")
    print("")










