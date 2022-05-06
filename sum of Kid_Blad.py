import nibabel as nib
import os
import numpy as np
import cv2


kid = '/home/has/Datasets/(reserve)kid_seg_nii'
kid_list = next(os.walk(kid))[2]
kid_list.sort()

blad = '/home/has/Datasets/_has_Task107_Blad_Kid'
blad_list = next(os.walk(blad))[1]
blad_list.sort()

print(kid_list)
print(blad_list)



for case in blad_list[433]:
    print(case)

    # kid_path = os.path.join(kid, kid_list[int(blad_list.index(case))-300])
    kid_path = os.path.join(kid, kid_list[-1])
    blad_path = os.path.join(blad, case, 'segmentation.nii.gz')

    print(kid_path)
    print(blad_path)


    blad_mask=nib.load(blad_path).get_fdata()
    kid_mask = nib.load(kid_path).get_fdata()


    z_axis = int(blad_mask.shape[0])

    vol_numpy = blad_mask + kid_mask


    xform = np.eye(4) * 2
    label_Nifti = nib.nifti1.Nifti1Image(vol_numpy, xform)

    bladder_name = case + '.nii.gz'

    path = '/home/has/Datasets/Kid_Blad_nii/'
    output_path = os.path.join(path,bladder_name)

    nib.save(label_Nifti, output_path)
    print("save nii")



