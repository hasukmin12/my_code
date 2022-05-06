import cv2
import numpy as np
from scipy.ndimage import zoom
import os
import nibabel as nib
from scipy.interpolate import RegularGridInterpolator

path = '/home/has/Datasets/ureter_overlap_rst/Ureter/Task_192_t73'
path_list = next(os.walk(path))[2]
path_list.sort()
print(path_list)

aim_path = '/home/has/Datasets/ureter_overlap_rst/Ureter/Task_192_t73_1mm'
if os.path.isdir(aim_path)==False:
    os.makedirs(aim_path)

for case in path_list[22:]:
    print("")
    print(case)
    seg_path = os.path.join(path, case)
    seg = nib.load(seg_path).get_fdata()
    print(seg.shape)

    # seg = zoom(seg, (5, 1, 1))
    #
    z_axis = int(seg.shape[0])
    # for z in range(0, z_axis):
    #     for x in range(0, 512):
    #         for y in range(0, 512):
    #             if seg[z][x][y] != 1:
    #                 if seg[z][x][y] != 2:
    #                     if seg[z][x][y] != 4:
    #                         seg[z][x][y] = 4

    xSize = 512
    ySize = 512
    z_axis_5mm = int(z_axis * 5)
    vol_numpy_seg = np.zeros((z_axis_5mm, xSize, ySize))

    # 0, 5, 10
    i = 0
    # for z in range(0, z_axis_5mm):
    #     if (z % 5) == 0:
    #         # print("z_axis 1mm : ", z)
    #         # print("z_axis 5mm : ", i)
    #         vol_numpy_seg[z, :, :] = seg[i, :, :]
    #         i += 1
    for z in range(0, z_axis_5mm):
        if (z % 5) == 0:
            vol_numpy_seg[z, :, :] = seg[i, :, :]
            i += 1
        else:
            vol_numpy_seg[z, :, :] = vol_numpy_seg[z-1, :, :]


    print(vol_numpy_seg.shape)

    xform = np.eye(4) * 2
    seg_Nifti = nib.nifti1.Nifti1Image(vol_numpy_seg, xform)
    output_path_seg = os.path.join(aim_path, case)
    print(seg_path)
    print(output_path_seg)
    nib.save(seg_Nifti, output_path_seg)


# width = 200
# height = 200
# img_stack_sm = np.zeros((len(img_stack), width, height))
# img_stack_sm = np.resize(img_stack, (100, 200, 200))
#
# for idx in range(len(img_stack)):
#     img = img_stack[idx, :, :]
#     img_sm = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
#     img_stack_sm[idx, :, :] = img_sm