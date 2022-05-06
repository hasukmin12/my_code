import nibabel as nib
import os
import numpy as np
import shutil


path = '/home/has/Datasets/CT_2_inference8_KiTS'
path_list = next(os.walk(path))[2]
path_list.sort()
print(path_list)

rst_path = '/home/has/Datasets/CT_2_inference9_KiTS_slice_100'
if os.path.isdir(rst_path) == False:
    os.makedirs(rst_path)



for case in path_list[161:]:
    kits_path = os.path.join(path,case)
    mask = nib.load(kits_path).get_fdata()
    print(case)
    print(mask.shape)
    z_axis = mask.shape[0]
    print(z_axis)
#
    numImage = z_axis//3
    print(numImage)

    i = 0
    xSize = 512
    ySize = 512
    vol_numpy = np.zeros((numImage+1, xSize, ySize))

    for z in range(0, z_axis):
        if z % 3 == 0 :
            # print(mask[z][:][:].max())
            vol_numpy[i][:][:] = mask[z][:][:]
            # print(vol_numpy[int][:][:].max())
            i += 1



    print("before : ", mask.shape)
    print("after : ",vol_numpy.shape)



    rst_path2 = os.path.join(rst_path, case)

    xform = np.eye(4) * 2
    label_Nifti = nib.nifti1.Nifti1Image(vol_numpy, xform)

    nib.save(label_Nifti, rst_path2)
    print(rst_path)
    print("save nii")
    print("")



