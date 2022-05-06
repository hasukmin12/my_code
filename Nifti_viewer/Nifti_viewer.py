import nibabel as nib
import os
import numpy as np


path = '/home/has/Datasets/_has_Task121_Urinary/case_00000/segmentation.nii.gz'

mask = nib.load(path).get_fdata()

print(mask.min())
print(mask.max())
print(mask.shape)

z_axis = int(mask.shape[0])
print(z_axis)

for z in range(0, z_axis):
    for x in range(0, 512):
        for y in range(0, 512):
            if mask[z][x][y] == 1:
                print(x,y,z)





