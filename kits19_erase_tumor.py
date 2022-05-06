import os
import nibabel as nib
import numpy as np

path = '/home/has/Datasets/kits19/data'
case_list = next(os.walk(path))[1]
case_list.sort()
print(case_list)

for case in case_list:


    case_path = os.path.join(path,case,'segmentation.nii.gz')
    img = nib.load(case_path).get_fdata()

    print(img.shape)
    z_axis = img.shape[0]

    for z in range(0,z_axis-1):
        for x in range(0, 512):
            for y in range(0, 512):
                if img[z][x][y] == 2:
                    img[z][x][y] = 0


    path_out_folder = '/home/has/Datasets/kits19_erase_tumor'
    path_out = os.path.join(path_out_folder,case)

    if os.path.isdir(path_out)==False:
        os.makedirs(path_out)

    img_case = os.path.join(path_out,'segmentation.nii.gz')

    xform = np.eye(4) * 2
    img_Nifti = nib.nifti1.Nifti1Image(img, xform)

    nib.save(img_Nifti, img_case)

