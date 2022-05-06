import os
import shutil

path = '/home/has/Datasets/_has_Task102_Bladder_reverse'
case_list = next(os.walk(path))[1]
case_list.sort()
print(case_list)

rst_path = '/home/has/Datasets/600_2_inference'
if os.path.isdir(rst_path)==False:
    os.makedirs(rst_path)
    print("make dir")

for case in case_list:
    print(case)
    img_path = os.path.join(path,case,'imaging.nii.gz')
    shutil.copyfile(img_path,os.path.join(rst_path,'CT_{0:03d}_0000.nii.gz'.format(case_list.index(case))))