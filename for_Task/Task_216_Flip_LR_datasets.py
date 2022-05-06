import nibabel as nib
import os
import numpy as np
import shutil
import cv2
import matplotlib.pyplot as plt




path = '/home/has/Datasets/_has_Task212_Ureter_5mm'
path_list = next(os.walk(path))[1]
path_list.sort()
print(path_list)


# rst_path = '/home/has/Datasets/_has_Task216_Ureter_5mm_LR'
# if os.path.isdir(rst_path) == False:
#     os.makedirs(rst_path)


for case in path_list:
    print(case)

    img_path = os.path.join(path,case,'imaging.nii.gz')
    mask_path = os.path.join(path,case,'segmentation.nii.gz')

    img = nib.load(img_path).get_fdata()
    mask = nib.load(mask_path).get_fdata()

    z_axis = int(img.shape[0])
    print("before slice, 1mm : ", img.shape)


    xSize = 512
    ySize = 512
    vol_numpy_img = np.zeros((z_axis, xSize, ySize))
    vol_numpy_seg = np.zeros((z_axis, xSize, ySize))


    for z in range(0, z_axis):

        # 그림RGB = cv2.cvtColor(그림BGR, cv2.COLOR_BGR2RGB)
        # img[z,:,:] = cv2.flip(img[z,:,:], 1) # 1은 좌우 반전, 0은 상하 반전입니다.

        vol_numpy_img[z, :, :] = cv2.flip(img[z,:,:], 0) # 1은 좌우 반전, 0은 상하 반전입니다.
        vol_numpy_seg[z, :, :] = cv2.flip(mask[z,:,:], 0)

        # 이 아래 부분은 그림을 화면에 출력하기 위한 부분으로, OpenCV 알고리즘과는 상관이 없습니다.

    # plt.figure("check", (12, 6))
    # plt.subplot(1, 2, 1)
    # plt.title("image")
    # plt.imshow(mask[40, :, :], cmap="gray")
    # plt.subplot(1, 2, 2)
    # plt.title("label")
    # plt.imshow(vol_numpy_seg[40, :, :])
    # plt.show()

    # num = path_list.index(case)
    rst_path_folder = os.path.join(path, "case_{0:05d}".format(path_list.index(case)+600))
    if os.path.isdir(rst_path_folder)== False:
        os.makedirs(rst_path_folder)
    rst_path_img = os.path.join(rst_path_folder, 'imaging.nii.gz')
    rst_path_seg = os.path.join(rst_path_folder, 'segmentation.nii.gz')
    xform = np.eye(4) * 2

    img_Nifti = nib.nifti1.Nifti1Image(vol_numpy_img, xform)
    seg_Nifti = nib.nifti1.Nifti1Image(vol_numpy_seg, xform)

    nib.save(img_Nifti, rst_path_img)
    nib.save(seg_Nifti, rst_path_seg)
    print(rst_path_img)
    print("save nii")
    print("")
