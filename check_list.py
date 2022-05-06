import os
import nibabel as nib

path = '/home/has/Datasets/_has_Task169_AVIEW_1mm'
path_list = next(os.walk(path))[1]
path_list.sort()

print(path_list)

for case in path_list[61:]:
    img_path = os.path.join(path,case,'imaging.nii.gz')
    seg_path = os.path.join(path,case,'segmentation.nii.gz')
    img = nib.load(img_path).get_fdata()
    seg = nib.load(seg_path).get_fdata()

    if img.shape != seg.shape:
        print(case)
        print(img.shape)
        print(seg.shape)
        print("")
