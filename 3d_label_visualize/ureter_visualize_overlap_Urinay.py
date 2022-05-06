import nibabel as nib
import os
import numpy as np
import shutil


path = '/home/has/Datasets/Ureter_only/case_00237/GT_seg.nii.gz'
path_inf = '/home/has/Datasets/Ureter_only/case_00237/inf_seg.nii.gz'

rst_path = '/home/has/Datasets/ureter_overlap_rst/Urinary'


GT_mask = nib.load(path).get_fdata()
inf_mask = nib.load(path_inf).get_fdata()

z_axis = int(inf_mask.shape[2])
print(z_axis)

for z in range(0, z_axis):
    for x in range(0, 512):
        for y in range(0, 512):
            if inf_mask[x][y][z] == 1:
                inf_mask[x][y][z] = 4


rst_mask = GT_mask + inf_mask

rst_path2 = os.path.join(rst_path, 'case_00237.nii.gz')

xform = np.eye(4) * 2
label_Nifti = nib.nifti1.Nifti1Image(rst_mask, xform)

nib.save(label_Nifti, rst_path2)
print(rst_path)
print("save nii")



