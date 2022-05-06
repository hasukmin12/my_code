import nibabel as nib
import os
import numpy as np
import shutil





path = '/home/has/Datasets/_has_ureter_overlap_rst/Ureter/Task_295_DDense'
path_list = next(os.walk(path))[2]
path_list.sort()
print(path_list)


rst_path = '/home/has/Datasets/_has_ureter_overlap_rst/5mm/Task_295_DDense'
if os.path.isdir(rst_path) == False:
    os.makedirs(rst_path)


for case in path_list:
    print(case)

    mask_path = os.path.join(path,case)
    img = nib.load(mask_path).get_fdata()

    z_axis = int(img.shape[0])
    print("before slice, 1mm : ", img.shape)


    xSize = 512
    ySize = 512
    z_axis_5mm = int(z_axis/5)
    vol_numpy_img = np.zeros((z_axis_5mm, xSize, ySize))

    # 0, 5, 10
    i = 0
    for z in range(0, z_axis):
        if (z%5) == 0:
            # print("z_axis 1mm : ", z)
            # print("z_axis 5mm : ", i)
            vol_numpy_img[i,:,:] =img[z,:,:]
            i += 1

    print("after slice, 5mm : ", vol_numpy_img.shape)


    rst_path_img = os.path.join(rst_path, case)
    xform = np.eye(4) * 2

    img_Nifti = nib.nifti1.Nifti1Image(vol_numpy_img, xform)
    nib.save(img_Nifti, rst_path_img)
    print(rst_path_img)
    print("save nii")
    print("")
