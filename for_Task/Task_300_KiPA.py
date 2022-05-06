import numpy as np
import os
import nibabel as nib
import shutil
join = os.path.join

path = '/home/has/Datasets/KiPA/train'
img_path = join(path, 'image')
seg_path = join(path, 'label')

path_list = next(os.walk(img_path))[2]
path_list.sort()
print(path_list)
print()


aim_path = '/home/has/Datasets/_has_KiPA'
if os.path.isdir(aim_path)== False:
    os.makedirs(aim_path)

for case in path_list:
    name = "case_{0:05d}".format(int(path_list.index(case)))
    input_img = join(img_path, case)
    output_dir = join(aim_path, name)
    if os.path.isdir(output_dir) == False:
        os.makedirs(output_dir)
    output_img = join(output_dir, 'imaging.nii.gz')

    input_seg = join(seg_path, case)
    output_seg = join(output_dir, 'segmentation.nii.gz')

    shutil.copyfile(input_img, output_img)
    shutil.copyfile(input_seg, output_seg)


