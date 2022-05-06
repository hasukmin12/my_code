import nibabel as nib
import os
import numpy as np
import shutil


path = '/home/has/Datasets/_has_Task128_Urinary'
aim_path = '/home/has/Datasets/_has_Bladder_red'
if os.path.isdir(aim_path) == False:
    os.makedirs(aim_path)
urinary_list = next(os.walk(path))[1]
urinary_list.sort()
# print(kid_blad_list)
print(urinary_list)



for case in urinary_list[240:]:
    print(case)

    urinary_path = os.path.join(path,case,'segmentation.nii.gz')
    print(urinary_path)
    urinary_mask = nib.load(urinary_path).get_fdata()


    z_axis = int(urinary_mask.shape[0])
    print(z_axis)


    for z in range(0, z_axis):
        for x in range(0, 512):
            for y in range(0, 512):
                if urinary_mask[z][x][y] == 1:
                    urinary_mask[z][x][y] = 0
                if urinary_mask[z][x][y] == 3:
                    urinary_mask[z][x][y] = 0
                if urinary_mask[z][x][y] == 2:
                    urinary_mask[z][x][y] = 1


    rst = urinary_mask
    print(rst.max())


    xform = np.eye(4) * 2
    label_Nifti = nib.nifti1.Nifti1Image(rst, xform)

    output_path = os.path.join(aim_path,"case_{0:05d}.nii.gz".format(urinary_list.index(case)))
    nib.save(label_Nifti, output_path)
    print(output_path)
    print("save nii")
    print("")



