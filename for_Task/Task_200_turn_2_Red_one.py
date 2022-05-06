
import skimage, os

import numpy as np

import cv2
try:
    import nibabel as nib
except:
    raise ImportError('Install NIBABEL')



input_path = '/home/has/Datasets/_has_Task196_Ureter_5mm/case_00509'
input_list = next(os.walk(input_path))[2]
input_list.sort()
print(input_list)



print("")
seg_path = os.path.join(input_path, 'segmentation.nii.gz')
seg = nib.load(seg_path).get_fdata()

# seg = seg.transpose(2,0,1)
print(seg.shape)

z_axis = int(seg.shape[0])
for z in range(0, z_axis):
    for x in range(0, 512):
        for y in range(0, 512):
            if seg[z][x][y] == 255:
                seg[z][x][y] = 1


xform = np.eye(4) * 2
seg_Nifti = nib.nifti1.Nifti1Image(seg, xform)
print("seg_max : ", seg.max())

output_path_seg = seg_path
print(seg_path)
print(output_path_seg)
nib.save(seg_Nifti, output_path_seg)
print("save nii")
print("")



