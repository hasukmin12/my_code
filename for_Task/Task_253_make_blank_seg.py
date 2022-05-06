import numpy as np
import os
import nibabel as nib


path = '/home/has/Datasets/_has_Task252_Ureter'
path_list = next(os.walk(path))[1]
path_list.sort()
print(path_list)


for case in path_list[361:]:

    img_path = os.path.join(path, case, 'imaging.nii.gz')
    img = nib.load(img_path).get_fdata()
    print(case)
    print(img.shape)
    z = img.shape[0]
    x = img.shape[1]
    y = img.shape[2]

    seg = np.zeros((z,x,y))
    print(seg.shape)
    print(seg.max())
    seg_out = os.path.join(path,case,'segmentation.nii.gz')

    xform = np.eye(4) * 2
    img_Nifti = nib.nifti1.Nifti1Image(seg, xform)
    nib.save(img_Nifti, seg_out)
    print("saved")
    print("")

