import os
import numpy as np
import nibabel as nib

path = '/home/has/Datasets/CT_half_up_bladder'
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

        z_axis = int(img.shape[0])
        # print(z_axis)
        # print(int(z_axis*(2/3)))


        # for z in range(0, int(z_axis*(5/10))):
        #     img = np.delete(img, z, axis=0)

        xSize = 512
        ySize = 512
        vol_numpy = np.zeros((int(z_axis*1/2),xSize, ySize))
        print(vol_numpy.shape)

        # print(img[100,:,:])

        for z in range(0, int(z_axis*(1/2))):
            # vol_numpy[z,:,:] = img[int(z_axis)-z+1,:,:]
            vol_numpy[z, :, :] = img[abs(z_axis-z-1), :, :]





        path_out = '/home/has/Datasets/CT_half_up_bladder_0_erase'
        if os.path.isdir(path_out)==False:
            os.makedirs(path_out)

        img_case = os.path.join(path_out, case)

        # img = img.transpose(1,2,0)
        print(vol_numpy.shape)

        xform = np.eye(4) * 2
        img_Nifti = nib.nifti1.Nifti1Image(vol_numpy, xform)


        nib.save(img_Nifti, img_case)



