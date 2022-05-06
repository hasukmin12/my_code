import os
import numpy as np
import nibabel as nib

path = '/home/has/Datasets/_has_600_2_inference'
blad_list = next(os.walk(path))[2]
blad_list.sort()
print(blad_list)



for case in blad_list:

    if case[-3:]=='.gz':

        case_path = os.path.join(path,case)

        img = nib.load(case_path).get_fdata()

        print("케이스 : ", case)
        print(img.shape)
        print(img.shape[0])

        z_axis = img.shape[0]
        # print(img)

        for z in range(0, z_axis):
            for x in range(0, 512):
                for y in range(0, 512):
                    if z < z_axis*(4/6):
                        img[z][x][y] = -1024



        path_out = '/home/has/Datasets/_has_600_2_inference_half'
        if os.path.isdir(path_out)==False:
            os.makedirs(path_out)

        img_case = os.path.join(path_out, case)

        img = img.transpose(1,2,0)
        print(img.shape)

        xform = np.eye(4) * 2
        img_Nifti = nib.nifti1.Nifti1Image(img, xform)


        nib.save(img_Nifti, img_case)



