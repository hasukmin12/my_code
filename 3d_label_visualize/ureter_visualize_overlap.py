import nibabel as nib
import os
import numpy as np
import shutil


# path = '/home/has/Datasets/Ureter_dataset_label(reverse)'
path_GT = '/home/has/Results/labelsTs(reverse)'
urinary_list = next(os.walk(path_GT))[2]
urinary_list.sort()
# print(kid_blad_list)
print(urinary_list)

# path_inf = '/home/has/Results/CT_2_inference_rst_120_e300(reverse)'
path_inf = '/home/has/Results/inf_2_GT_140(reverse)'
inf_list = next(os.walk(path_inf))[2]
inf_list.sort()
print(inf_list)


rst_path = '/home/has/Datasets/ureter_overlap_rst/Ureter/Task_140'
if os.path.isdir(rst_path)==False:
    os.makedirs(rst_path)


for case in urinary_list:
    print(case)

    GT_path = os.path.join(path_GT,case)
    # inf_path = os.path.join(path_inf, case)
    inf_path = os.path.join(path_inf, inf_list[urinary_list.index(case)])

    GT_mask = nib.load(GT_path).get_fdata()
    inf_mask = nib.load(inf_path).get_fdata()


    z_axis = int(inf_mask.shape[2])
    print(z_axis)

    for z in range(0, z_axis):
        for x in range(0, 512):
            for y in range(0, 512):
                if inf_mask[x][y][z] == 1:
                    inf_mask[x][y][z] = 4


    rst_mask = GT_mask + inf_mask
    # rst_mask = rst_mask.transpose(1,2,0)
    print(rst_mask.shape)
    print(rst_mask.min())
    print(rst_mask.max())

    rst_path2 = os.path.join(rst_path, case)

    xform = np.eye(4) * 2
    label_Nifti = nib.nifti1.Nifti1Image(rst_mask, xform)

    nib.save(label_Nifti, rst_path2)
    print(rst_path)
    print("save nii")



