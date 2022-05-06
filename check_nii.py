import os
import nibabel as nib

# path = '/home/has/Datasets/kits19/data'
path = '/home/has/Datasets/_has_Task185_AVIEW_1mm_reverse'

path_list = next(os.walk(path))[1]
path_list.sort()

print(path_list)

for case in path_list[102:]:
    img_path = os.path.join(path,case,'imaging.nii.gz')
    seg_path = os.path.join(path,case,'segmentation.nii.gz')
    img = nib.load(img_path).get_fdata()
    seg = nib.load(seg_path).get_fdata()
    # print(case)
    # print(img.shape)
    # print(seg.shape)


    if img.shape != seg.shape:
        print(case)
        print(img.shape)
        print(seg.shape)
        print("")
