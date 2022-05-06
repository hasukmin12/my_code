import numpy as np
import os
import nibabel as nib
import shutil


path = '/home/has/Datasets/_has_Task273_Urinary'
path_list = next(os.walk(path))[1]
path_list.sort()
print(path_list)

kid_path = '/home/has/Datasets/_has_Task128_Urinary'
kid_list = next(os.walk(kid_path))[1]
kid_list.sort()
print(kid_list)

for case in kid_list:
    print()
    print(case)
    kid_case_path = os.path.join(kid_path, case, 'segmentation.nii.gz')
    kid = nib.load(kid_case_path).get_fdata()
    z_axis = int(kid.shape[0])
    case_folder = os.path.join(path, case)

    if os.path.isdir(os.path.join(path,case))==True:
        aim_path = os.path.join(path, case, 'segmentation.nii.gz')
        img = nib.load(aim_path).get_fdata()

        for z in range(0, z_axis):
            for x in range(0, 512):
                for y in range(0, 512):
                    if kid[z][x][y] == 2:
                        img[z][x][y] = 2
                    if kid[z][x][y] == 3:
                        img[z][x][y] = 3

        # seg_out = os.path.join(path,case,'segmentation.nii.gz')

        xform = np.eye(4) * 2
        img_Nifti = nib.nifti1.Nifti1Image(img, xform)
        nib.save(img_Nifti, aim_path)
        print("saved")
        print("")



    # Ureter 제외한 신장 방광만 사용하자
    else:
        os.makedirs(case_folder)

        input = os.path.join(kid_path,case,'imaging.nii.gz')
        output = os.path.join(case_folder, 'imaging.nii.gz')
        shutil.copyfile(input, output)

        # for z in range(0, z_axis):
        #     for x in range(0, 512):
        #         for y in range(0, 512):
        #             if kid[z][x][y] == 1:
        #                 kid[z][x][y] = 0

        seg_out = os.path.join(case_folder, 'segmentation.nii.gz')

        xform = np.eye(4) * 2
        img_Nifti = nib.nifti1.Nifti1Image(kid, xform)
        nib.save(img_Nifti, seg_out)
        print("saved")
        print("")

