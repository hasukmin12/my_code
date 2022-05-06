
import skimage, os

import numpy as np

import cv2
try:
    import nibabel as nib
except:
    raise ImportError('Install NIBABEL')



input_path = '/home/has/Datasets/_has_Task195_Ureter_1mm'
input_list = next(os.walk(input_path))[1]
input_list.sort()
print(input_list)


for case in input_list:

    seg_path = os.path.join(input_path, case, 'segmentation.nii.gz')
    seg = nib.load(seg_path).get_fdata()

    if seg.max() !=1:
        print(case)
