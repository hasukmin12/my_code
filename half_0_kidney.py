import os
import numpy as np
import nibabel as nib

path = '/home/has/Datasets/kits19/data'
blad_list = next(os.walk(path))[1]
blad_list.sort()
print(blad_list)

path_out = '/home/has/Datasets/kits19_half3'
if os.path.isdir(path_out)==False:
    os.makedirs(path_out)


for case in blad_list:


    case_path = os.path.join(path,case, 'imaging.nii.gz')

    img = nib.load(case_path).get_fdata()

    print("케이스 : ", case)
    print(img.shape)
    print(img.shape[0])

    z_axis = img.shape[0]
    # print(img)

    for z in range(0, z_axis):
        for x in range(0, 512):
            for y in range(0, 512):
                if z > z_axis*(4/6):
                    img[z][x][y] = -1024


    img_case = os.path.join(path_out, case)
    if os.path.isdir(img_case)==False:
        os.makedirs(img_case)

    img_path = os.path.join(img_case,'imaging.nii.gz')

    # img = img.transpose(1,2,0)
    # print(img.shape)

    xform = np.eye(4) * 2
    img_Nifti = nib.nifti1.Nifti1Image(img, xform)


    nib.save(img_Nifti, img_path)




# case_path = os.path.join(path,'CT_000_0000.nii.gz')
#
# img = nib.load(case_path).get_fdata()
# print(img.shape)
# # img = img.transpose(1, 2, 0)
# # print(img.shape)
#
# print(img.shape[0])
#
# z_axis = img.shape[0]
#
# for z in range(0,z_axis-1):
#     for x in range(0, 512):
#         for y in range(0, 512):
#             if z>40:
#                 img[z][x][y] = 0