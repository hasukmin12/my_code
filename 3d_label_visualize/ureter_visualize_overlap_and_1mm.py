import nibabel as nib
import os
import numpy as np
import shutil

path_GT = '/home/has/Results/labelsTs'
urinary_list = next(os.walk(path_GT))[2]
urinary_list.sort()
print(urinary_list)

path_inf = '/home/has/Results/inf_2_GT_275_Dense'
inf_list = next(os.walk(path_inf))[2]
inf_list.sort()
print(inf_list)


rst_path = '/home/has/Datasets/_has_ureter_overlap_rst/Ureter/Task_275_Dense'
if os.path.isdir(rst_path)==False:
    os.makedirs(rst_path)


for case in urinary_list:
    print()
    print(case)

    GT_path = os.path.join(path_GT,case)
    inf_path = os.path.join(path_inf, inf_list[urinary_list.index(case)])

    GT_mask = nib.load(GT_path).get_fdata()
    inf_mask = nib.load(inf_path).get_fdata()

    # print(GT_mask.shape)
    # print(inf_mask.shape)

    z_axis = int(inf_mask.shape[0])
    # print(z_axis)
    # print(inf_mask.shape)

    for z in range(0, z_axis):
        for x in range(0, 512):
            for y in range(0, 512):
                if inf_mask[z][x][y] == 2:
                    inf_mask[z][x][y] = 0

    for z in range(0, z_axis):
        for x in range(0, 512):
            for y in range(0, 512):
                if inf_mask[z][x][y] == 3:
                    inf_mask[z][x][y] = 0


    for z in range(0, z_axis):
        for x in range(0, 512):
            for y in range(0, 512):
                if inf_mask[z][x][y] == 1:
                    inf_mask[z][x][y] = 2

    rst_mask = GT_mask + inf_mask

    for z in range(0, z_axis):
        for x in range(0, 512):
            for y in range(0, 512):
                if rst_mask[z][x][y] == 3:
                    rst_mask[z][x][y] = 4

    print(rst_mask.shape)
    # print(rst_mask.min())
    print(rst_mask.max())

    xSize = 512
    ySize = 512
    z_axis_5mm = int(z_axis * 5)
    vol_numpy_seg = np.zeros((z_axis_5mm, xSize, ySize))

    # 0, 5, 10
    i = 0

    for z in range(0, z_axis_5mm):
        if (z % 5) == 0:
            vol_numpy_seg[z, :, :] = rst_mask[i, :, :]
            i += 1
        else:
            vol_numpy_seg[z, :, :] = vol_numpy_seg[z - 1, :, :]

    print(vol_numpy_seg.shape)


    rst_path2 = os.path.join(rst_path, case)

    xform = np.eye(4) * 2
    label_Nifti = nib.nifti1.Nifti1Image(vol_numpy_seg, xform)

    nib.save(label_Nifti, rst_path2)
    print(rst_path)
    print("save nii")
    print("")



