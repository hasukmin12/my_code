import numpy as np # linear algebra

import skimage, os
import numpy as np

import cv2

import os
import nibabel as nib


# path = '/home/has/Results/CT_2_inference_rst_146_soft_map'
path = '/home/has/Datasets/_has_Task210_Ureter_5mm'
path_out = '/home/has/Datasets/_has_Task210_Ureter_5mm_reverse'
if os.path.isdir(path_out) == False:
    os.makedirs(path_out)

path_list = next(os.walk(path))[1]
path_list.sort()

print(path_list)


for case in path_list:

    img_path = os.path.join(path, case, 'imaging.nii.gz')
    seg_path = os.path.join(path,case, 'segmentation.nii.gz')

    img = nib.load(img_path).get_fdata()
    seg = nib.load(seg_path).get_fdata()
    print("")
    print(case)
    print(img.shape)
    #print(seg.shape)

    # img = img.transpose(1,2,0)
    img = img.transpose(1,2,0)
    seg = seg.transpose(1,2,0)

    print(img.shape)

    img_out_dir = os.path.join(path_out, case)
    if os.path.isdir(img_out_dir) == False:
        os.makedirs(img_out_dir)

    img_out = os.path.join(path_out, case, 'imaging.nii.gz')
    seg_out = os.path.join(path_out, case, 'segmentation.nii.gz')
    print(img_path)
    print(img_out)
    print("")


    xform = np.eye(4) * 2
    img_Nifti = nib.nifti1.Nifti1Image(img, xform)
    label_Nifti = nib.nifti1.Nifti1Image(seg, xform)

    nib.save(img_Nifti, img_out)
    nib.save(label_Nifti, seg_out)