import nibabel as nib
import os
import numpy as np
import shutil




path = '/home/has/Results/inf_2_GT_124(reverse)/case_00027.nii.gz'
# path = '/home/has/Datasets/test2/case_00000/segmentation.nii.gz'
rst_path = '/home/has/Datasets/Ureter_only/case_00237'
if os.path.isdir(rst_path)==False:
    os.makedirs(rst_path)


mask = nib.load(path).get_fdata()

z_axis = int(mask.shape[2])
print(z_axis)

for z in range(0, z_axis):
    for x in range(0, 512):
        for y in range(0, 512):
            if mask[x][y][z] == 2:
                mask[x][y][z] = 0
            elif mask[x][y][z] == 3:
                mask[x][y][z] = 0




rst_path2 = os.path.join(rst_path, 'inf_seg.nii.gz')

xform = np.eye(4) * 2
label_Nifti = nib.nifti1.Nifti1Image(mask, xform)

nib.save(label_Nifti, rst_path2)
print(rst_path)
print("save nii")



