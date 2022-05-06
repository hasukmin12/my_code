
import skimage, os
import shutil
import numpy as np

import cv2
try:
    import nibabel as nib
except:
    raise ImportError('Install NIBABEL')



input_path = '/home/has/Datasets/_has_Task220_Ureter_5mm'
input_list = next(os.walk(input_path))[1]
input_list.sort()
print(input_list)

aim_path = '/home/has/Datasets/_has_Task240_Ureter_LR_half'
if os.path.isdir(aim_path) == False:
    os.makedirs(aim_path)



for case in input_list:
    print("")
    print(case)
    img_path = os.path.join(input_path, case, 'imaging.nii.gz')
    output_path_dir = os.path.join(aim_path, case)
    if os.path.isdir(output_path_dir)==False:
        os.makedirs(output_path_dir)
    output_path_img = os.path.join(output_path_dir, 'imaging.nii.gz')
    print(img_path)
    print(output_path_img)
    shutil.copyfile(img_path, output_path_img)


    seg_path = os.path.join(input_path, case, 'segmentation.nii.gz')
    seg = nib.load(seg_path).get_fdata()

    # seg = seg.transpose(2,0,1)
    print(seg.shape)

    # for z in range(0, z_axis):
    #     for x in range(256, 512):
    #         for y in range(0, 512):
    #             if seg[z][x][y] == 1:
    #                 seg[z][x][y] = 6



    z_axis = int(seg.shape[0])

    z_list = []

    for z in range(0, z_axis):
        if seg[z].max() == 1:
            z_list.append(z)


    print(z_list)
    z_min = int(z_list[0])
    z_max = int(z_list[-1])
    z_half = int((z_min+z_max)/2)
    print(z_half)


    for z in range(z_min, z_half):     # half
        for x in range(256, 512):  # LR
            for y in range(0, 512):
                if seg[z][x][y] == 1:
                    seg[z][x][y] = 3

    for z in range(z_half, z_max):
        for x in range(256, 512):
            for y in range(0, 512):
                if seg[z][x][y] == 1:
                    seg[z][x][y] = 2


    for z in range(z_min, z_half):
        for x in range(0, 256):
            for y in range(0, 512):
                if seg[z][x][y] == 1:
                    seg[z][x][y] = 4




    xform = np.eye(4) * 2
    seg_Nifti = nib.nifti1.Nifti1Image(seg, xform)
    print("seg_max : ", seg.max())

    output_path_seg = os.path.join(output_path_dir, 'segmentation.nii.gz')
    print(output_path_seg)
    nib.save(seg_Nifti, output_path_seg)
    print("save nii")
    print("")



